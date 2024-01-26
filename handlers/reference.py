import sqlite3
from aiogram import types, Dispatcher
from config import bot
from database.databases import DataBase
from keyboards import inline_buttons
from aiogram.utils.deep_linking import _create_link
import os
import binascii
from const import REFERENCE_MENU_TEXT


async def reference_menu_call(call: types.CallbackQuery):
    db = DataBase()
    data = db.kipoha_select_user_referral(
        owner=call.from_user.id
    )
    await bot.send_message(
        chat_id=call.from_user.id,
        text=REFERENCE_MENU_TEXT.format(
            user=call.from_user.first_name,
            total=data['total_referrals']
        ),
        reply_markup=await inline_buttons.referral_keyboard()
    )


async def generate_link(call: types.CallbackQuery):
    db = DataBase()
    user = db.kipoha_select_user(tg_id=call.from_user.id)
    if not user['link']:
        token = binascii.hexlify(os.urandom(8)).decode()
        link = await _create_link("start", payload=token)
        print(link)
        db.kipoha_update_link(
            link=link,
            tg_id=call.from_user.id
        )
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Here is ur new link: {user['link']}",
        )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Here is ur old link: {user['link']}",
        )

async def referal_list(call: types.CallbackQuery):
    db = DataBase()
    result = db.kipoha_get_referral(ref_tg_id=call.from_user.id)
    if not result:
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Your referal is none"
        )
        return
    text = ''
    n = 0
    for t in result:
        n += 1
        text += f"{n}. {t[2]}"

    await bot.send_message(
        chat_id=call.from_user.id,
        text=text
    )
    print(result)

async def check_balance(call: types.CallbackQuery):
    db = DataBase()
    try:
        db.kipoha_add_wallet(
            tg_id=call.from_user.id
        )
    except sqlite3.IntegrityError:
        pass
    money = db.kipoha_get_wallet(
        tg_id=call.from_user.id
    )
    await bot.send_message(
        chat_id=call.from_user.id,
        text=f"Your balance {money['balance']}"
    )


def reg_reference_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        reference_menu_call,
        lambda call: call.data == "reference_menu"
    )
    dp.register_callback_query_handler(
        generate_link,
        lambda call: call.data == "generate_link"
    )
    dp.register_callback_query_handler(
        referal_list,
        lambda call: call.data == "list_ref_link"
    )
    dp.register_callback_query_handler(
        check_balance,
        lambda call: call.data == "check_bal"
    )