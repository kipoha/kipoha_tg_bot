import sqlite3

from aiogram import types, Dispatcher
from config import bot, MEDIA_DESTINATION
from database import databases
from keyboards import inline_buttons
from const import START_MENU


async def kipoha_start(message: types.Message):
    db = databases.DataBase()
    try:
        db.kipoha_add_user(
            tg_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )
    except sqlite3.IntegrityError:
        pass

    print(message)
    # await bot.send_message(
    #     chat_id=message.from_user.id,
    #     text=f"Hello {message.from_user.first_name}",
    #     reply_markup=await inline_buttons.kipoha_start_keyboard()
    # )

    with open(MEDIA_DESTINATION + "1705332202502.png", "rb") as ph:
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=ph,
            caption=START_MENU.format(
                name=message.from_user.first_name
            ),
            reply_markup=await inline_buttons.kipoha_start_keyboard()
        )

def reg_kipoha_start_handlers(dp: Dispatcher):
    dp.register_message_handler(kipoha_start, commands=['start'])
