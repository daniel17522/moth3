from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


async def reply_webapp(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    geeks_online = KeyboardButton('Geeks Online', web_app=types.WebAppInfo(url='https://online.geeks.kg/'))

    youtube = KeyboardButton('YouTube', web_app=types.WebAppInfo(url='https://www.youtube.com/'))

    spotify = KeyboardButton('Spotify', web_app=types.WebAppInfo(url='https://open.spotify.com/'))

    jutsu = KeyboardButton('Jutsu', web_app=types.WebAppInfo(url='https://jut.su/'))

    netflix = KeyboardButton('Netflix', web_app=types.WebAppInfo(url='https://www.netflix.com/'))

    kinocrad = KeyboardButton('kinocrad', web_app=types.WebAppInfo(url='https://kinokrad.ac/'))

    keyboard.add(geeks_online, youtube, spotify, jutsu, netflix, kinocrad)

    await message.answer(text='WebApp кнопки.', reply_markup=keyboard)



async def inline_webapp(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=2, resize_keyboard=True)

    gitignore_io = InlineKeyboardButton('ignore.io', web_app=types.WebAppInfo(url='https://docs.gitignore.io/'))

    keyboard.add(gitignore_io)

    await message.answer('WebApp кнопки.', reply_markup=keyboard)
def register_handler_webapp(dp: Dispatcher):
    dp.register_message_handler(reply_webapp, commands=['reply_webapp'])
    dp.register_message_handler(inline_webapp, commands=['inline'])