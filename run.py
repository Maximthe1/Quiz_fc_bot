import asyncio

from aiogram import Dispatcher, Bot, types
from aiogram.filters import Command

from app.config import TOKEN
from app.handlers.quest_handlers import questrt
from app.handlers.main_handlers import rt


bot = Bot(token=TOKEN)
dp = Dispatcher()


dp.include_router(router=rt)
dp.include_router(router=questrt)


async def run():
	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot)
 
 
if __name__ == "__main__":
	try:
		asyncio.run(run())
	except (KeyboardInterrupt, SystemExit):
		print("Выключение...")