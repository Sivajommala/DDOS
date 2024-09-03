import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from flask import Flask
from threading import Thread

# Function to handle all messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('𝗥𝗔𝗠 𝗥𝗔𝗠 ❤')

# Keep alive function
app = Flask('')

@app.route('/')
def home():
    return "I am alive"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Main function to set up the bot
def main():
    # Start the keep-alive server
    keep_alive()

    # Get the bot token from environment variables
    bot_token = os.getenv("BOT_TOKEN")

    # Create the Application and pass it your bot's token
    application = ApplicationBuilder().token(bot_token).build()

    # Add a message handler for all text messages
    application.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
