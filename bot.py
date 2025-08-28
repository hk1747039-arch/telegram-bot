import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from flask import Flask
from threading import Thread

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable not set")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(m: Message):
    await m.answer("✅ Bot is running!")

async def run_bot():
    await dp.start_polling(bot)

# --- keepalive web ---
app = Flask(__name__)
@app.route("/")
def home():
    return "Bot is alive!"

def run_flask():
    app.run(host="0.0.0.0", port=3000)

if __name__ == "__main__":
    Thread(target=run_flask).start()
    asyncio.run(run_bot())
