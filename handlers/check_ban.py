from aiogram import types, Dispatcher
from config import bot
from database import databases
from keyboards import inline_buttons

async def check_ban(call: types.CallbackQuery):
    db = databases.DataBase()
    banned = db.kipoha_check_ban_user(call.from_user.id)
    if banned:
        ban_count = banned[2]
        await bot.send_message(
            chat_id=call.from_user.id,
            text=f"Your ban count: {ban_count}"
        )
        print('banned')
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="You're not on the banlist"
        )
        print('not banned')
    # await bot.send_message(
    #     chat_id=call.from_user.id,
    #     text="banned"
    # )
    # print('banned')

def register_bans_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(check_ban,
                                       lambda call: call.data == "bans")