import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Токен бота в переменной окружения BOT_TOKEN
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я простой бот.")

# Точка входа
if __name__ == "__main__":
    # Создаём приложение бота
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Добавляем команду /start
    app.add_handler(CommandHandler("start", start))
    
    # Запускаем бота
    print("Бот запущен...")
    app.run_polling()
