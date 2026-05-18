import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def start(message: types.Message):
    await message.answer("Bot works!")

executor.start_polling(dp)
