import os
from dotenv import load_dotenv

#получить список слов, хранящихся в файле vocab.py
from vocab import vocab

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

from telegram import Update, ForceReply
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

user_data = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    # Очистим старые данные
    user_data[chat_id] = {}
    await update.message.reply_text("Привет! Выбери на каком языке бот будет выдавать слова: напиши 'английский' или 'русский'.")

async def handle_language_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    lang = update.message.text.lower()
    if lang in ['английский', 'русский']:
        user_data[chat_id] = {"lang": lang}
        await send_word(update, context)
    else:
        await update.message.reply_text("Пожалуйста, укажи на каком языке боту присылать слова, напиши 'английский' или 'русский'.")

async def send_word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    data = user_data[chat_id]
    lang = data["lang"]

    import random
    word_en = random.choice(list(vocab.keys()))
    word_ru = vocab[word_en]

    if lang == "английский":
        data["current_word"] = word_en
        data["expected_answer"] = word_ru
        await update.message.reply_text(f"Translate: {word_en}")
    else:
        data["current_word"] = word_ru
        data["expected_answer"] = word_en
        await update.message.reply_text(f"Переведи: {word_ru}")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text = update.message.text.strip().lower()

    if chat_id not in user_data or "lang" not in user_data[chat_id]:
        if text in ['английский', 'русский']:
            user_data[chat_id] = {"lang": text}
            await send_word(update, context)
        else:
            await update.message.reply_text("Пожалуйста, укажи на каком языке боту присылать слова, напиши 'английский' или 'русский'.")
    else:
        if "expected_answer" not in user_data[chat_id]:
            await update.message.reply_text("Произошла ошибка. Попробуй /start сначала.")
            return

        user_answer = update.message.text.strip().lower().replace("’", "'")
        correct_answer = user_data[chat_id]["expected_answer"].strip().lower().replace("’", "'")


        if user_answer == correct_answer:
            await update.message.reply_text("✅ Done!")
            await send_word(update, context)  # даём следующее слово
        else:
            await update.message.reply_text(f"❌ Incorrect. Correct answer: {correct_answer}")
            # Повторно просим перевести то же слово
            lang = user_data[chat_id]["lang"]
            current_word = user_data[chat_id]["current_word"]
            if lang == "английский":
                await update.message.reply_text(f"Try again: {current_word}")
            else:
                await update.message.reply_text(f"Попробуй ещё раз: {current_word}")

app = ApplicationBuilder().token(TOKEN).build()


app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()