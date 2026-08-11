from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Salam! Mən Morvyn AI Assistant 🤖\n\n"
        "🎮 PUBG məsləhətləri\n"
        "🎬 YouTube ideyaları\n"
        "🌍 Tərcümə\n"
        "✍️ Mətn yazmaq\n\n"
        "Sualını yaz 😎"
    )

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "pubg" in text:
        reply = "🎮 PUBG üçün 4-finger gyro və sensitivity məsləhətləri verə bilərəm."

    elif "youtube" in text:
        reply = "🎬 YouTube üçün başlıq, təsvir və thumbnail ideyaları hazırlaya bilərəm."

    elif "salam" in text:
        reply = "Salam 👋 Mən Morvyn AI Assistant 🤖"

    else:
        reply = f"🤖 Morvyn AI düşünür...\n\nSənin mesajın:\n{text}"

    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

print("🤖 Morvyn AI Render-də aktivdir...")
app.run_polling()
