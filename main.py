import os
import sys
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from handlers import setup_handlers
import telegram

# Загрузка переменных окружения
load_dotenv()

# Получаем токены и настройки из .env
TOKEN = os.getenv("TELEGRAM_TOKEN")
PORT = int(os.getenv("PORT", 10000))
RENDER_URL = os.getenv("RENDER_URL")

# Отладочная информация
print("Python version:", sys.version)
print("PTB version:", telegram.__version__)
print("Poker Bot запущен!")

# Создание и запуск приложения
app = ApplicationBuilder().token(TOKEN).build()
setup_handlers(app)

if __name__ == "__main__":
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{RENDER_URL}/{TOKEN}"
    )
