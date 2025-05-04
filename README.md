# 📚 Telegram Vocabulary Bot

Простой Telegram-бот для тренировки перевода слов между английским и русским языками.

## 🚀 Возможности

- Перевод слов с английского на русский и наоборот
- Выбор направления перевода пользователем
- Обратная связь: правильно/неправильно
- Простая логика и расширяемая структура

## 🧠 Используемые технологии

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- Python 3.10+
- `dotenv` для защиты токена
- Хостинг на [Render.com](https://render.com)

## 🔐 Настройка

1. Клонируй проект:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
Установи зависимости:

bash
Копировать
Редактировать
pip install -r requirements.txt
Создай .env файл и добавь свой токен:

ini
Копировать
Редактировать
BOT_TOKEN=your_telegram_bot_token
Запусти локально:

bash
Копировать
Редактировать
python tgbot.py
☁️ Развёртывание на Render
Запушь проект на GitHub

Перейди в Render Dashboard

Создай New Web Service

Укажи:

Build Command: pip install -r requirements.txt

Start Command: python tgbot.py

Environment Variables: добавь BOT_TOKEN

Готово!

🧩 Пример взаимодействия
markdown
Копировать
Редактировать
/start
> Привет! Выбери язык: английский или русский
> Переведи: dog
< собака
> ✅ Done!
📁 Структура
bash
Копировать
Редактировать
.
├── tgbot.py          # Основной код бота
├── .env              # Переменные окружения (не пушить!)
├── .gitignore
├── requirements.txt
└── README.md
🛠 В планах
Добавить больше слов

Добавить уровни сложности

Сохранять прогресс пользователя

Разделение кода на модули

📬 Контакты
Если возникли вопросы или идеи — пишите в Telegram: @emtuse
