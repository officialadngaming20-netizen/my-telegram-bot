import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ⚠️ Token is NOT written here directly (safe method)
TOKEN = os.getenv("8687174945:AAH6b2YdzKa9rQ_0nM-sGrRydzWXHPyD81E")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! Your bot is working successfully.")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Commands: /start /help")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
