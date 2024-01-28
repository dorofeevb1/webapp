from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


inlbtn=[
    [InlineKeyboardButton(text="Старт", callback_data="openWebApps")]

]



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


inline_kb = InlineKeyboardMarkup(inline_keyboard=inlbtn)
keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True, selective=True)

