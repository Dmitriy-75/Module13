from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = '7931532450:AAEqh_lc8MhvdhzX6ydjy_m_c6flhFhPPIA'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def all_message(massage):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_message(massage):
    print('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor. start_polling(dp, skip_updates=True)


