from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters
from tournament import Tournament
from utils import load_players, save_players

tournament = Tournament()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот для управления покерным турниром. Введите /setup для начала.")

async def setup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Введите бай-ин, ребай и аддон через пробел, например:\n`100 50 25`", parse_mode="Markdown")
    return

async def handle_setup_values(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        buy_in, rebuy, addon = map(int, update.message.text.split())
        tournament.set_prices(buy_in, rebuy, addon)
        await update.message.reply_text(f"Установлено:\nБай-ин: {buy_in}\nРебай: {rebuy}\nАддон: {addon}\n\nТеперь используйте /addplayer")
    except:
        await update.message.reply_text("Ошибка ввода. Попробуйте снова, пример:\n`100 50 25`", parse_mode="Markdown")

async def add_player(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Введите имя игрока:")
    return

async def handle_player_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.text.strip()
    tournament.add_player(name)
    save_players(tournament.players)
    await update.message.reply_text(f"Игрок {name} добавлен. Используйте /rebuy, /addon или /results.")

async def rebuy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(name, callback_data=f"rebuy_{name}")]
                for name in tournament.players.keys()]
    await update.message.reply_text("Выберите игрока для ребая:", reply_markup=InlineKeyboardMarkup(keyboard))

async def addon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(name, callback_data=f"addon_{name}")]
                for name in tournament.players.keys()]
    await update.message.reply_text("Выберите игрока для аддона:", reply_markup=InlineKeyboardMarkup(keyboard))

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    action, name = query.data.split("_")
    if action == "rebuy":
        tournament.add_rebuy(name)
        await query.edit_message_text(f"Ребай добавлен игроку {name}")
    elif action == "addon":
        tournament.add_addon(name)
        await query.edit_message_text(f"Аддон добавлен игроку {name}")
    save_players(tournament.players)

async def results(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = tournament.get_results()
    await update.message.reply_text(text)

def setup_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("setup", setup))
    app.add_handler(CommandHandler("addplayer", add_player))
    app.add_handler(CommandHandler("rebuy", rebuy))
    app.add_handler(CommandHandler("addon", addon))
    app.add_handler(CommandHandler("results", results))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_setup_values))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_player_name))
    app.add_handler(CallbackQueryHandler(button_handler))
