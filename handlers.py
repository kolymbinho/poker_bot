from telegram.ext import CommandHandler, MessageHandler, filters

def start(update, context):
    update.message.reply_text("Бот работает!")

def setup_handlers(app):
    app.add_handler(CommandHandler("start", start))
