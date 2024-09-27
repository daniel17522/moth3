import logging
from aiogram.utils import executor
from buttons import start_test
from config import bot, dp, admin
from handlers import commands, echo, quiz, FSM_registration, fsm_store, webapp, admin_group, send_products, update_products
from db import db_main

async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text="Бот включен!",
                               reply_markup=start_test)
        await db_main.sql_create()


commands.register_commands(dp)
quiz.register_quiz(dp)
FSM_registration.register_fsm_reg(dp)
fsm_store.register_store(dp)
webapp.register_handler_webapp(dp)
send_products.register_send_products_handler(dp)
update_products.register_update_products_handler(dp)
admin_group.register_admin_group(dp)
#echo.register_echo(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)