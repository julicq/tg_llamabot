from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from llama_cpp import Llama
from huggingface_hub.file_download import http_get
import os

# Initialize your Llama model and other constants
# MODEL_PATH = "/models/model-q4_K.gguf"
SYSTEM_PROMPT = "Ты - русскоязычный ассистент. Ты разговариваешь с людьми и помогаешь им."

def get_message_tokens(model, role, content):
    content = f"{role}\n{content}\n</s>"
    content = content.encode("utf-8")
    return model.tokenize(content, special=True)

def get_system_tokens(model):
    system_message = {"role": "system", "content": SYSTEM_PROMPT}
    return get_message_tokens(model, **system_message)

def load_model(
    directory: str = ".",
    model_name: str = "model-q4_K.gguf",
    model_url: str = "https://huggingface.co/julicq/model-q4_K/blob/main/model-q4_K.gguf"
):
    final_model_path = os.path.join(directory, model_name)
    
    print("Downloading all files...")
    if not os.path.exists(final_model_path):
        with open(final_model_path, "wb") as f:
            http_get(model_url, f)
    os.chmod(final_model_path, 0o777)
    print("Files downloaded!")
    
    model = Llama(
        model_path=final_model_path,
        n_ctx=1024
    )
    
    print("Model loaded!")
    return model

MODEL = load_model()

# Define command handler for /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я - твой русскоязычный ассистент.')

# Define message handler for text messages
def handle_message(update: Update, context: CallbackContext) -> None:
    message_text = update.message.text
    # Process message and generate response using your model
    response = generate_response(message_text)
    # Send response back to the user
    update.message.reply_text(response)

# Function to generate response using your model
def generate_response(message_text: str) -> str:
    # Get tokens for the system prompt
    system_tokens = get_system_tokens(MODEL)

    # Initialize tokens with system prompt tokens
    tokens = system_tokens[:]

    # Get tokens for the user's message
    user_message_tokens = get_message_tokens(model=MODEL, role="user", content=message_text)

    # Extend tokens with user's message tokens
    tokens.extend(user_message_tokens)

    # Generate response using the model
    response = ""
    generator = MODEL.generate(tokens, top_k=30, top_p=0.9, temp=0.01)

    for i, token in enumerate(generator):
        if token == MODEL.token_eos():
            break
        response += MODEL.detokenize([token]).decode("utf-8", "ignore")

    return response

# Get Telegram bot token from environment variable
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater(TELEGRAM_BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))

    # Register message handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
