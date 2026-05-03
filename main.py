from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8687174945:AAHU5oDb1ZBIdUafP_-7f6Trjajdkt5BHjg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Bot is working ✅")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
