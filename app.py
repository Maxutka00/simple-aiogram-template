from aiogram import executor
from aiogram import types
import settings
from loader import dp
import errors, handlers

async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await dispatcher.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
        ]
    )


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
