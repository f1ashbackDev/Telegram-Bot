from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from hadlers.database import CreateUser

class saveCity(StatesGroup):
    selectedCity = State()

async def selectCity(message: types.message, state: FSMContext):
    await state.update_data(city = message.text.lower())
    user_data = await state.get_data()
    await CreateUser(user = message.from_user.id, city = user_data['city'])
    #await saveRaduis.raduis.set()

def register_handler_citySelection(dp : Dispatcher):
    dp.register_message_handler(selectCity, state=saveCity.selectedCity)