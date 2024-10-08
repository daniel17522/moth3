from aiogram import types, Dispatcher
from config import bot, admin


async def welcome_user(message: types.Message):
    for member in message.new_chat_members:
        await message.answer(f'Добро пожаловать, {member.full_name}\n\n'
                             f'Правило группы:\n'
                             f'Не материться!\n'
                             f'Не спамить\n')


words = ['дурак', 'тупой', 'козёл', 'овца']


async def filter_words(message: types.Message):
    messege_text = message.text.lower()
    for word in words:
        if word in messege_text:
            await message.answer('Не ругайся')
            await message.delete()
            break


user_warnings = {}

async def user_warning(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in admin:
            await message.answer('Ты не админ!')
        elif not message.reply_to_message:
            await message.answer('Команда должна быть ответом на сообщение!')
        else:
            user_id = message.reply_to_message.from_user.id
            user_name = message.reply_to_message.from_user.full_name
            user_warnings[user_id] = user_warnings.get(user_id, 0) +1

            for Admin in admin:
                await bot.send_message(chat_id=Admin,
                                       text=f'{user_name} получил предупреждение {user_warnings}/3')

            if user_warnings[user_id] >= 3:
                await bot.kick_chat_member(message.chat.id, user_id)
                await bot.unban_chat_member(message.chat.id, user_id)
                await bot.send_message(chat_id=Admin,)


def register_admin_group(dp: Dispatcher):
    dp.register_message_handler(welcome_user, content_types=[types.ContentTypes.NEW_CHAT_MEMBERS])

    dp.register_message_handler(filter_words)
