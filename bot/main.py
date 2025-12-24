from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import asyncio

TOKEN = "8468368861:AAGk4rgo85ufxi2eR2w1eo9DaUIdpYowSxg"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("uzbekistan"))
async def start(message: Message):
    await message.answer("Poytaxt: Toshkent Axoli soni: 37 mln")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
