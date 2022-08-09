import asyncio
import config as config
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import BotBlocked
from hadlers.citySelection import register_handler_citySelection

from hadlers.common import register_handler_common
from hadlers.siteSection import register_hanlder_url
from hadlers.user import register_handler_user

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

#Регистрация команд
async def set_commands(bot: Bot):
    commands = [
        bot.BotCommand(command="/start", description="Начать работу с ботом")        
    ]
    await bot.set_my_commands(commands)

#Обработка ошибок бота
@dp.errors_handler(exception = BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")
    return True

async def main():
    #Установка команд бота
    #await set_commands(bot)
    
    #Регистрируем все функции бота
    register_handler_common(dp)
    register_hanlder_url(dp)
    register_handler_user(dp)
    register_handler_citySelection(dp)

    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())