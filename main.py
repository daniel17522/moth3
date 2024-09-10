import logging
from aiogram import types
from aiogram.utils import executor
import os
from buttons import start, start_test
from config import bot, dp, admin
from handlers import commands, echo, quiz, FSM_registration



async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text="Бот включен!",
                    reply_markup=start_test)

commands.register_commands(dp)

quiz.register_quiz(dp)

FSM_registration.register_FSM(dp)

echo.register_echo(dp)




if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)




