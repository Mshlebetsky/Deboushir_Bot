import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from app.config import TOKKEN
from app.handlers import users, admin

from app.db.engine import engine, Base
from app.db import models

async def main():
    Base.metadata.create_all(bind=engine)

    bot = Bot(
        TOKKEN,
        default=DefaultBotProperties(parse_mode="HTML")
    )

    dp = Dispatcher()

    dp.include_router(users.router)
    dp.include_router(admin.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
