import sqlite3
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from aiogram.dispatcher.filters import Text

def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    SELECT * FROM products p
    INNER JOIN product_details pd ON p.product_id = pd.product_id
    """).fetchall()
    conn.close()
    return products

def delete_product(product_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM products WHERE product_id + ?", (product_id,))
    conn.commit()
    conn.close()

async def start_sending(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)

    button = InlineKeyboardButton('Все товары', callback_data='show_all_delete')
    keyboard.add(button)

    await message.answer('Если нажать на кнопку ниже, выйдут все товары разом!',
                         reply_markup=keyboard)


async def send_all_products(callback_query: types.CallbackQuery):
    products = fetch_all_products()

    if products:
        for product in products:
            caption = (f"Название товара - {product['name_product']}\n"
                       f"Информация о товаре - {product['info_product']}\n"
                       f"категория - {product['category']}\n"
                       f"Размер - {product['size']}\n"
                       f"Цена - {product['price']}\n"
                       f"Артикул - {product['product_id']}\n")
            await callback_query.message.answer_photo(photo=product['photo'],
                                                      caption=caption)
        else:
            await callback_query.message.answer("Товары не найдены!")


async def delete_product_callback(callback_query: types.CallbackQuery):
    product_id = int(callback_query.data.split('_')[1])
    delete_product(product_id)
    await callback_query.answer('Товар удалён')




