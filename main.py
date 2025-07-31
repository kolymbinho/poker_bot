from telegram.ext import ApplicationBuilder
from handlers import setup_handlers
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()
setup_handlers(app)

if __name__ == "__main__":
    print("Poker Bot запущен!")
    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.getenv("PORT", 10000)),
        webhook_url=f"{os.getenv('RENDER_EXTERNAL_URL')}{TOKEN}"
    )
