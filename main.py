import keyboard
import asyncio

from aiogram import Bot, Dispatcher, types
from config import TOKEN, WEBAPP_URL
from aiogram.filters import CommandStart, Command
from aiogram.types import BotCommand, Message, InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime, timedelta
from handlers import handlers

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    user_id = message.from_user.id
    current_time = datetime.now()

    # Проверяем, использовал ли пользователь функцию сегодня
    if user_id in handlers.last_accessed and (current_time - handlers.last_accessed[user_id]).days < 1:
        inl = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Старт",
                                      web_app=types.WebAppInfo(url=WEBAPP_URL, mode='fullscreen', fullscreen=True))]
            ]
        )
        await message.answer("Поздравляем🎉\n Вы присоединились к сообществу\nдуховно развивающихся людей!\n"
                             "Вы можете открыть карты нажав\nкнопку Старт", reply_markup=inl)
    else:
        # Убедитесь, что WEBAPP_URL определен
        inl = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Старт", web_app=types.WebAppInfo(url=WEBAPP_URL, mode='fullscreen', fullscreen=True))]
            ]
        )
        await message.answer("Поздравляем🎉\n Вы присоединились к сообществу\nдуховно развивающихся людей!\n"
                             "Вы можете открыть карты нажав\nкнопку Старт", reply_markup=inl)
        handlers.user_bonuses[user_id] = handlers.user_bonuses.get(user_id, 0) + 3
        handlers.last_accessed[user_id] = current_time

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