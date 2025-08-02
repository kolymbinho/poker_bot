import os
from telegram.ext import ApplicationBuilder
from handlers import setup_handlers
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

setup_handlers(app)

# ✅ Webhook-запуск
app.run_webhook(
    listen="0.0.0.0",
    port=int(os.environ.get("PORT", 10000)),
    webhook_url=f"{os.getenv('RENDER_URL')}/{TOKEN}",
)
