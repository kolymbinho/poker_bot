import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
RENDER_URL = os.getenv("RENDER_URL")
PORT = int(os.getenv("PORT", 10000))


# ✅ Пример хендлера команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Бот работает 🔥")


# ✅ Создание приложения
app = ApplicationBuilder().token(TOKEN).build()

# ✅ Регистрируем хендлеры
app.add_handler(CommandHandler("start", start))


# ✅ Запуск через Webhook
if __name__ == "__main__":
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=f"{RENDER_URL}/{TOKEN}"
    )
