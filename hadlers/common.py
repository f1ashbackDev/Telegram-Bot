from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

buttons = [
    'Показать все объявления',
    'Выложить свое объявление',
    'Повесить отслеживание объявления',
    'Проверить автомобиль',
    'Профиль',
    'Настройки бота',
    'О боте'
]

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboardAbout = types.ReplyKeyboardMarkup(resize_keyboard=True)

keyboardAbout.add("Назад")

for name in buttons:
    keyboard.add(name)

async def cmd_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        f"Привет, {message.from_user.first_name}!\nВыбери действия", 
        reply_markup=keyboard
    )

async def cmd_return(message: types.message, state: FSMContext):
    await state.finish()
    await message.answer(
        "Выберите действия",
        reply_markup= keyboard
    )

async def cmd_about(message: types.message):
    keyboard.add()
    await message.answer(
        "Разработчик бота:\n@f1ashbackss\nСсылки:\nhttps://github.com/f1ashbackDev",
        reply_markup = keyboardAbout
    )

def register_handler_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands = "start", state = "*")
    dp.register_message_handler(cmd_return, lambda msg: msg.text.lower() == 'назад', state = "*")
    dp.register_message_handler(cmd_about, lambda msg: msg.text.lower() == 'о боте',)
