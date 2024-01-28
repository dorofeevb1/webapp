import keyboard
import asyncio

from aiogram import Bot, Dispatcher
from config import TOKEN
from aiogram.filters import CommandStart, Command
from aiogram.types import BotCommand, Message


bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Поздравляем🎉\n Вы присоединились к сообществу\nдуховно развивающихся людей!\n"
                             "Вы можете открыть карты нажав\nкнопку Старт", reply_markup=keyboard.inline_kb)
    await message.answer("Или используйте меню ниже:", reply_markup=keyboard.keyboard)



async def main():
    from handlers.handlers import dp
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())