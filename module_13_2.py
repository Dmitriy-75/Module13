# Выполните все действия представленные в предыдущих видео модуля, создав и подготовив Telegram-бот для дальнейших
# заданий. Нужные версии для 13 и 14 модулей и вашего виртуального окружения находятся здесь. Если не помните,
# как установить необходимые библиотеки, обратитесь к материалам 11 модуля. Актуальная версия Python для дальнейшей
# работы - 3.9.13.
#
# Задача "Бот поддержки (Начало)": К коду из подготовительного видео напишите две асинхронные функции: start(message)
# - печатает строку в консоли 'Привет! Я бот помогающий твоему здоровью.' . Запускается только когда написана команда
# '/start' в чате с ботом. (используйте соответствующий декоратор) all_massages(message) - печатает строку в консоли
# 'Введите команду /start, чтобы начать общение.'. Запускается при любом обращении не описанном ранее. (используйте
# соответствующий декоратор) Запустите ваш Telegram-бот и проверьте его на работоспособность.



from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = 'Ключ'
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


