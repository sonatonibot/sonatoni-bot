import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

async def start(update, context):
    await update.message.reply_text("নমস্কার! আমি সনাতনী বট। চালু হয়ে গেছি।")

async def reply(update, context):
    await update.message.reply_text("হরে কৃষ্ণ! তোমার মেসেজ পেয়েছি।")

def main():
    token = os.environ.get("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    app.run_polling()

if __name__ == "__main__":
    main()
