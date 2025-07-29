import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from handlers import setup_handlers

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
PORT = int(os.getenv("PORT", "10000"))
RENDER_URL = os.getenv("RENDER_URL")

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    setup_handlers(application)
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=f"{RENDER_URL}/{TOKEN}"
    )

if __name__ == "__main__":
    main()
