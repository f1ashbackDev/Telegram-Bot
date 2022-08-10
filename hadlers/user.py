from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from hadlers.citySelection import saveCity
from middlewares.database import getUserData, getUserCity

buttons = [
    'Показать объявление',
    'Фильтр',
    'Назад'
]

filters = {
    'city': '',
    'radius':'',
    'nameCar': '',
    'modelCar': '',
    'typeCar': ''
}

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

for name in buttons:
    keyboard.add(name)

class userData(StatesGroup):
    city = State()

async def checkCars_Start(message: types.message, state: FSMContext):
    checkUser = await getUserData(user = message.from_user.id)
    
    print(await state.get_data())

    if checkUser != None:
        await message.answer(
            f"Выбери действия", 
            reply_markup=keyboard
        )
    else:
        await message.answer("Для начала просмотра объявлений вам нужно указать город. Укажите город",
            reply_markup = types.ReplyKeyboardRemove())
        await saveCity.selectedCity.set()

async def filtersCars(message: types.message):
    loadSettings = await getUserCity(user = message.from_user.id)
    print('фильтр')

def register_handler_user(dp: Dispatcher):
    dp.register_message_handler(checkCars_Start, lambda msg: msg.text.lower() == 'показать все объявления')
    dp.register_message_handler(filtersCars, lambda msg: msg.text.lower() == 'фильтр')