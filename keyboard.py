from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton






kb=[
    [
        KeyboardButton(text='Старт'),
        KeyboardButton(text='Описание'),
    ],
    [
        KeyboardButton(text='Счет'),
        KeyboardButton(text='Пригласить друга')
    ]
]

keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True, selective=True)

