#                          Домашнее задание по теме "Клавиатура кнопок".


# Цель: научится создавать клавиатуры и кнопки на них в Telegram-bot.
#
# Задача "Меньше текста, больше кликов": Необходимо дополнить код предыдущей задачи, чтобы вопросы о параметрах тела
# для расчёта калорий выдавались по нажатию кнопки. Измените massage_handler для функции set_age. Теперь этот хэндлер
# будет реагировать на текст 'Рассчитать', а не на 'Calories'. Создайте клавиатуру ReplyKeyboardMarkup и 2 кнопки
# KeyboardButton на ней со следующим текстом: 'Рассчитать' и 'Информация'. Сделайте так, чтобы клавиатура
# подстраивалась под размеры интерфейса устройства при помощи параметра resize_keyboard. Используйте ранее созданную
# клавиатуру в ответе функции start, используя параметр reply_markup. В итоге при команде /start у вас должна
# присылаться клавиатура с двумя кнопками. При нажатии на кнопку с надписью 'Рассчитать' срабатывает функция set_age
# с которой начинается работа машины состояний для age, growth и weight.



from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

api = 'Ключ'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


k = ReplyKeyboardMarkup()
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
k.add(button1, button2)
kb = k.resize_keyboard



class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет. Я бот, помогающий твоему здоровью', reply_markup=kb)


@dp.message_handler(text=['Рассчитать'])
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growht(message, state):
    await state.update_data(age=int(message.text))
    await message.answer(f"Введите свой рост")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer(f"Введите свой вес")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()

    calories = 10*(data['weight']) + 6*(data['growth']) - 5*(data['age']) + 5

    await message.answer(f"Ваша норма калорий = {calories}")
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start')


if __name__ == '__main__':
    executor. start_polling(dp, skip_updates=True)


