from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import logging
from datetime import datetime


# Replace with your actual bot token
TELEGRAM_BOT_TOKEN = '7719772505:AAF1bwLSGKg1ZSUMic7z9NAjyfSUh4UNRyg'

# Logging config
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s',
    level=logging.INFO
)

# Message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text
    log_line = f"From {user.username or user.id}: {text}\n"

    now = datetime.now()
    formatted = now.strftime("%Y-%m-%d %H:%M")
    file_name = str(formatted)+'.txt'
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(log_line)

    await update.message.reply_text("Message received and logged!")

# Entry point: no asyncio.run(), no async def main()
if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("Bot is running...")
    app.run_polling()  # <- Blocking call, no event loop conflicts
