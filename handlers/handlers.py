from aiogram.filters.command import Command
from aiogram import types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import WEBAPP_URL
from main import dp, bot

@dp.message(Command('start'))
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Open WebApp",
                                  web_app=types.WebAppInfo(url=WEBAPP_URL, mode='fullscreen', fullscreen=True))]
        ]
    )
    await message.answer("Hello! Click the button below to open the WebApp.", reply_markup=keyboard)

