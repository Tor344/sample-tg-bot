import asyncio

from aiogram import Bot, Dispatcher
import config.settings as set
from app.start.handlers import router as start_router
from app.user.handlers import router as user_router
from app.admin.handlers import router as admin_router

from config.logging_admin import loger
from app.database.repository import db


bot = Bot(token=set.API_TOKEN)
dp = Dispatcher()


dp.include_router(user_router)
dp.include_router(admin_router)
dp.include_router(start_router)


async def main():
    try:
        await db.connect()
        loger.info("Бот запущен")
        await dp.start_polling(bot)
    except Exception as e:
        await db.close()
    finally:
        await db.close()



if __name__ == "__main__":
    asyncio.run(main())