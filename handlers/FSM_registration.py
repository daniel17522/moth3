from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


# Finite State Machine - машина состояния, FSM
class FSM_reg(StatesGroup):
    fullname = State()
    date = State()
    email = State()
    phone = State()
    addres = State()
    gender = State()
    country = State()
    photo = State()


async def start_fsm_reg(message: types.Message):
    await message.answer('Введите фио:')
    await FSM_reg.fullname.set()


async def load_fullname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname'] = message.text

        await message.answer('Введите дату рождения')
        await FSM_reg.next()


async def load_date(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
        await message.answer('Введите email')
        await FSM_reg.next()


async def load_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
        await message.answer('Введите номер телефона')
        await FSM_reg.next()


async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
        await message.answer('Введите адрес')
        await FSM_reg.next()


async def load_addres(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['addres'] = message.text
        await message.answer('Введите пол/гендер')
        await FSM_reg.next()


async def load_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text
        await message.answer('Введите страну проживания')
        await FSM_reg.next()


async def load_country(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['country'] = message.text
        await message.answer('Скиньте фото')
        await FSM_reg.next()


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

        await message.answer_photo(photo=data['photo'],
                                   caption=f'Верны ли данные \n\n'
                                           f'ФИО: {data["fullname"]}\n'
                                           f'дата рождения: {data["date"]}\n'
                                           f'Эл.Почта: {data["email"]}\n'
                                           f'Номер телефона: {data["phone"]}\n'
                                           f'Адрес: {data["addres"]}\n'
                                           f'Пол: {data["gender"]}\n'
                                           f'страна: {data["country"]}\n')

        await state.finish()
def register_FSM(dp: Dispatcher):
    dp.register_message_handler(start_fsm_reg, commands=['reg'])
    dp.register_message_handler(load_fullname, state=FSM_reg.fullname)
    dp.register_message_handler(load_date, state=FSM_reg.date)
    dp.register_message_handler(load_email, state=FSM_reg.email)
    dp.register_message_handler(load_phone, state=FSM_reg.phone)
    dp.register_message_handler(load_addres, state=FSM_reg.addres)
    dp.register_message_handler(load_gender, state=FSM_reg.gender)
    dp.register_message_handler(load_country, state=FSM_reg.country)
    dp.register_message_handler(load_photo, state=FSM_reg.photo,
                                content_types=['photo'])
