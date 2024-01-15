from aiogram import Bot, Dispatcher, types
import asyncio
from config import TOKEN, WEBAPP_URL

bot = Bot(token=TOKEN)
dp = Dispatcher()
async def main():
    from handlers.handlers import dp
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped!")
