import asyncio
import logging
from app.handlers import rt
from app.btconf import bot
from aiogram import Dispatcher


async def main():
    logging.basicConfig(level=logging.DEBUG)
    dp = Dispatcher()
    dp.include_router(rt)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

