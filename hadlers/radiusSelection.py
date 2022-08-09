from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

#class saveRaduis(State):
#    raduis = State()

async def selectRadius(message: types.message, state: FSMContext):
    print('Дошёл до сюда')

async def saveRadiusUser(user, radius):
    pass

#def register_handler_select_raduis(dp: Dispatcher):
#    dp.register_message_handler(selectRadius, state = saveRaduis.raduis)