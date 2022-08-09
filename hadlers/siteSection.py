from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

url_sites = [
    'Avito.ru', 
    'Auto.ru'
]

class SaveUrl(StatesGroup):
    waiting_url_sites = State()

async def siteSectionStart(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for name in url_sites:
        keyboard.add(name)
    await message.answer("Выберите сайты с которых хотите получать уведомление!",
                        reply_markup=keyboard)
    await SaveUrl.waiting_url_sites.set()

async def siteSection(message: types.message, state: FSMContext):
    await state.update_data(choose_url=message.text.lower())
    user_data = await state.get_data()
    await message.answer("32131123", reply_markup=types.ReplyKeyboardRemove())
    
#Регистрируем
def register_hanlder_url(dp : Dispatcher):
    dp.register_message_handler(siteSectionStart, commands="test", state = "*")
    dp.register_message_handler(siteSection, state=SaveUrl.waiting_url_sites)

