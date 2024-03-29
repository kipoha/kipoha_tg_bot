import random
import sqlite3

from aiogram import types, Dispatcher

import database.databases
from config import bot, MEDIA_DESTINATION
from database import databases
from keyboards import inline_buttons
from const import START_MENU
from aiogram.utils.deep_linking import _create_link
# from scraping.anecdot import NewsScraper
# from scraping.newscraping import AsyncNewsScraper
import asyncio


async def kipoha_start(message: types.Message):
    db = databases.DataBase()
    try:
        db.kipoha_add_user(
            tg_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )
        db.kipoha_add_wallet(
            tg_id=message.from_user.id
        )
    except sqlite3.IntegrityError:
        pass

    print(message)
    # await bot.send_message(
    #     chat_id=message.from_user.id,
    #     text=f"Hello {message.from_user.first_name}",
    #     reply_markup=await inline_buttons.kipoha_start_keyboard()
    # )

    print(message.get_full_command())
    command = message.get_full_command()

    if command[1] != "":
        link = await _create_link('start', payload=command[1])
        owner = db.kipoha_select_user_by_link(
            link=link
        )
        if owner['telegram_id'] == message.from_user.id:
            await bot.send_message(
                chat_id=message.from_user.id,
                text="U can not use own link!!!"
            )
            return

        try:
            ref = db.kipoha_get_referral(
                ref_tg_id=message.from_user.id,
            )
            if not ref:
                db.kipoha_add_referral(
                    owner=owner['telegram_id'],
                    referral=message.from_user.id,
                    referral_name=message.from_user.first_name
                )
                db.kipoha_update_bal_referral(
                    tg_id=owner['telegram_id'],
                )
        except sqlite3.IntegrityError:
            pass

    with open(MEDIA_DESTINATION + "1705332202502.png", "rb") as ph:
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=ph,
            caption=START_MENU.format(
                name=message.from_user.first_name
            ),
            reply_markup=await inline_buttons.kipoha_start_keyboard()
        )
#
# async def random_anecdot(call: types.CallbackQuery):
#     db = databases.DataBase()
#     scraper = AsyncNewsScraper()
#     texts = await scraper.get_data()
#     text = random.choice(texts)
#     text = text.replace('<div class="text">', '')
#     text = text.replace('<br>', '\n')
#     text = text.replace('</div>', '')
#     await bot.send_message(
#         chat_id=call.from_user.id,
#         text=text,
#         reply_markup=await inline_buttons.anecdots_keyboard()
#     )
#     db.kipoha_add_anecdot(
#         text=text,
#         tg_id=call.from_user.id,
#         username=call.from_user.first_name
#     )

    # scraper = NewsScraper()
    # data = scraper.parse_data()
    #
    # text = random.choice(data)
    #
    # text = text.replace('<div class="text">', '')
    # text = text.replace('<br>', '\n')
    # text = text.replace('</div>', '')
    # await bot.send_message(
    #     chat_id=call.from_user.id,
    #     text=text,
    #     reply_markup=await inline_buttons.anecdots_keyboard()
    # )
    # db.kipoha_add_anecdot(
    #     text=text,
    #     tg_id=call.from_user.id,
    #     username=call.from_user.first_name
    # )

async def kipoha_start_button(call: types.CallbackQuery):

    with open(MEDIA_DESTINATION + "1705332202502.png", "rb") as ph:
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=ph,
            caption=START_MENU.format(
                name=call.from_user.first_name
            ),
            reply_markup=await inline_buttons.kipoha_start_keyboard()
        )


def reg_kipoha_start_handlers(dp: Dispatcher):
    dp.register_message_handler(kipoha_start, commands=['start'])
    # dp.register_callback_query_handler(random_anecdot, lambda call: call.data == 'anecdots')
    # dp.register_callback_query_handler(kipoha_start_button, lambda call: call.data == 'back_to_start')
