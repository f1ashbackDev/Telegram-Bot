from hadlers.citySelection import saveCity
from hadlers.database import getUserData
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

buttons = [
    'Показать объявление',
    'Фильтр',
    'Назад'
]

keyboard = types.ReplyKeyboardMarkup(resize_keyboard= True)

for nameButton in buttons:
    keyboard.add(nameButton)

class userData(StatesGroup):
    city = State()

async def checkCars_Start(message: types.message, state:FSMContext):
    checked = await getUserData(user = message.from_user.id)
    if checked != None:
       await state.update_data(city = "Чувашия")
       await message.ReplyKeyboardMarkup(keyboard)
    else:
        await message.answer("Для начала просмотра объявлений вам нужно указать город. Укажите город",
            reply_markup = types.ReplyKeyboardRemove())
        await saveCity.selectedCity.set()

def register_handler_user(dp: Dispatcher):
    dp.register_message_handler(checkCars_Start, lambda msg: msg.text.lower() == 'показать все объявления')