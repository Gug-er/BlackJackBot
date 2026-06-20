import asyncio

from aiogram import Bot, Dispatcher

from src.config import settings
from src.bot.handlers.commands import router as commands_router

async def main():
    bot = Bot(token=settings.TOKEN)
    dp = Dispatcher()

    dp.include_router(commands_router)
    
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    asyncio.run(main())

