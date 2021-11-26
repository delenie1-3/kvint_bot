import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage#машина состояний

from app.config_reader import load_config
from app.handlers.pizza import register_handlers_pizza
from app.handlers.common import register_handlers_common

#функция для команд бота
async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/pizza", description="Заказать пиццу"),
        BotCommand(command="/cancel", description="Отменить текущее действие")
    ]
    await bot.set_my_commands(commands)

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/pizza", description="Заказать пиццу"),
        BotCommand(command="/cancel", description="Отменить текущее действие")
    ]
    await bot.set_my_commands(commands)

#основная функция запуска
async def main():
    # Чтение файла конфигурации
    config = load_config("config/bot.ini")

    # Объявление и инициализация бота и диспетчера
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher(bot, storage=MemoryStorage())

    # Регистрация хэндлеров
    register_handlers_common(dp)
    register_handlers_pizza(dp)

    # Установка команд бота
    await set_commands(bot)

    # Запуск поллинга
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())