# Telegram Bot with Llama Model Integration

This project is a Telegram bot that integrates the Llama language model to interact with users in Russian. The bot responds to messages and commands, providing a conversational AI experience.

## Features

- Responds to the `/start` command with a greeting.
- Handles text messages and generates responses using the Llama language model.
- Automatically downloads and loads the Llama model if not present locally.
- Processes messages with a system prompt to maintain context.

## Installation

### Prerequisites

- Python 3.7+
- Telegram bot token (You can get one from [BotFather](https://core.telegram.org/bots#botfather))

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/telegram-llama-bot.git
   cd telegram-llama-bot

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

3. Set up your environment variables. Create a .env file in the root directory and add your Telegram bot token:

    ```
    TELEGRAM_BOT_TOKEN=your-telegram-bot-token

4. Run the bot:

    ```bash
    python tg_chatbot_v3.py

### Usage

- Start the bot by sending the **/start** command in your Telegram chat.
- Send any text message to the bot, and it will respond using the Llama language model.

### Project Structure
- **tg_chatbot_v3.py**: Main script that sets up the Telegram bot and integrates the Llama model.
- **requirements.txt**: Python dependencies required for the project.

### Contributing
1. Fork the repository.
2. Create a new branch (**git checkout -b feature/your-feature**).
3. Make your changes and commit them (**git commit -am 'Add your feature'**).
4. Push to the branch (**git push origin feature/your-feature**).
5. Create a new Pull Request.

### License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/julicq/tg_llamabot/blob/main/LICENSE) file for details.

### Acknowledgements
[Llama](https://github.com/julicq/llama) for the language model.
[Hugging Face](https://huggingface.co/) for model hosting and API.

Feel free to customize the README.md file according to your specific project details and requirements.
