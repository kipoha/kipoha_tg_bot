# from aiogram import types, Dispatcher
# from config import bot
# from database import databases
# from keyboards import inline_buttons
# from config import bot, MEDIA_DESTINATION
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from const import PROFILE_TEXT
#
# class UpdateProfileStates(StatesGroup):
#     nickname = State()
#     bio = State()
#     age = State()
#     zodiac_sigh = State()
#     games = State()
#     country = State()
#     photo = State()
#
#
# async def update_profile(call: types.CallbackQuery):
#     await bot.send_message(
#         chat_id=call.from_user.id,
#         text='Select your profile',
#         reply_markup=await inline_buttons.kipoha_select_profile_button()
#     )
#
# def reg_update_profile_handlers(dp: Dispatcher):
#     dp.register_callback_query_handler(
#         update_profile,
#     lambda call: call.data == "pr_update"
#     )