import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from handlers import setup_handlers
import telegram

# Загрузка .env
load_dotenv()

# Переменные окружения
TOKEN = os.getenv("TELEGRAM_TOKEN")
PORT = int(os.getenv("PORT", 10000))
RENDER_URL = os.getenv("RENDER_URL")

# Отладочная информация
print("Python version:", telegram.__version__)
print("Poker Bot запущен!")

# Создание и запуск бота
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    setup_handlers(app)
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{RENDER_URL}/{TOKEN}"
    )
