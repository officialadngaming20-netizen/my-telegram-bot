import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# SAFE: token loaded from environment variable
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome! Your bot is running successfully.")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot Commands:\n"
        "/start - Start bot\n"
        "/help - Show help"
    )

def main():
    if not TOKEN:
        print("❌ ERROR: TOKEN is missing. Add it in environment variables.")
        return

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
