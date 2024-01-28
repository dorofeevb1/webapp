from datetime import datetime, timedelta
from aiogram import types, F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import WEBAPP_URL
from main import dp

last_accessed = {}
user_bonuses = {}


@dp.callback_query(F.data == "openWebApps")
async def openWebApps(callback: CallbackQuery):
    user_id = callback.message.from_user.id
    current_time = datetime.now()

    # Проверяем, использовал ли пользователь функцию сегодня
    if user_id in last_accessed and (current_time - last_accessed[user_id]).days < 1:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Карты ангелов",
                                      web_app=types.WebAppInfo(url=WEBAPP_URL, mode='fullscreen', fullscreen=True))]
            ]
        )
        await callback.message.answer("HЧтобы открыть карты ангелов, нажми кнопку ниже", reply_markup=keyboard)
    else:
        # Убедитесь, что WEBAPP_URL определен
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Карты ангелов", web_app=types.WebAppInfo(url=WEBAPP_URL, mode='fullscreen', fullscreen=True))]
            ]
        )
        await callback.message.answer("Чтобы открыть карты ангелов, нажми кнопку ниже", reply_markup=keyboard)
        user_bonuses[user_id] = user_bonuses.get(user_id, 0) + 3
        last_accessed[user_id] = current_time


@dp.message(F.text.lower() == "старт")
async def openWebApps(message: types.Message):
    user_id = message.from_user.id
    current_time = datetime.now()

    # Проверяем, использовал ли пользователь функцию сегодня
    if user_id in last_accessed and (current_time - last_accessed[user_id]).days < 1:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Карты ангелов",
                                      web_app=types.WebAppInfo(url=WEBAPP_URL, mode='fullscreen', fullscreen=True))]
            ]
        )
        await message.answer("Чтобы открыть карты ангелов, нажми кнопку ниже", reply_markup=keyboard)
    else:
        # Убедитесь, что WEBAPP_URL определен
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Карты ангелов", web_app=types.WebAppInfo(url=WEBAPP_URL, mode='fullscreen', fullscreen=True))]
            ]
        )
        await message.answer("Чтобы открыть карты ангелов, нажми кнопку ниже", reply_markup=keyboard)
        user_bonuses[user_id] = user_bonuses.get(user_id, 0) + 3
        last_accessed[user_id] = current_time


@dp.message(F.text.lower() == "описание")
async def stat(message: types.Message):

    await message.answer("Это карты Ангелов записанные на человеческий язык методом ченнелинга\n"
                         "Если есть запрос - у Ангелов есть ответ\n"
                         "Карты помогают человеку найти вектор куда двигаться в своей ситуации\n"
                         "Либо В течении дня\n"
                         "Либо какой то серьёзный вопрос\n\n"
                         "Вы можете выбрать карту 1 раз в день\n"
                         "Допускается выбирать карты много раз,\n"
                         "Но чтобы это работало рекомендуется придать уважение этому инструменту\n"
                         "И не заигрываться\n"
                         "1 раз выбрать карту - получить ответ = точно работает\n\n"
                         "Для того, чтобы ангелы вам помогли, нужно сформулировать запрос на этот день. Это может быть задача, сложная ситуация, или просто необходимая мотивация или подсказка. Как только вы сформулировали запрос, нажимайте кнопку Начать\n\n"
    "За работу с картами вы получаете бонус-рубли, которые потом можно сконвертировать в реальные деньги в рамках обучения в нашей школе.\n"
    "Про школу информацию вы получите в конце работы с картами Ангелов\n")


@dp.message(F.text.lower() == "счет")
async def start(message: types.Message):
    user_id = message.from_user.id
    # Показываем текущий баланс бонусов пользователя
    bonus_amount = user_bonuses.get(user_id, 0)
    await message.answer(f"Ваш баланс бонусов: {bonus_amount}")


@dp.message(F.text.lower() == "пригласить друга")
async def invite_friend(message: types.Message):
    user_id = message.from_user.id
    # Создаем уникальную ссылку для приглашения
    invite_link = f"https://t.me/sadsjhewyweufcnsBot?start={user_id}"

    # Сообщение с инструкцией и ссылкой
    invite_message = f"Пригласите своих друзей использовать нашего бота! Отправьте им эту ссылку: {invite_link}\n\nВы получите бонусы за каждого приглашенного друга!"

    await message.answer(invite_message)
