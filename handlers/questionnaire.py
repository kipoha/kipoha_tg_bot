from aiogram import types, Dispatcher
from config import bot
from database import databases
from keyboards import inline_buttons


async def kipoha_question(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Which module is better to choose with the Discord API?",
        reply_markup=await inline_buttons.first_question()
    )

async def disnake_answers(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="A good choice! it supports the latest version of the Discord API and works stably",
        reply_markup=await inline_buttons.kipoha_question2(),
    )

async def discord_answers(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="This module is quite old, but a lot of people use it",
        reply_markup=await inline_buttons.kipoha_question2(),
    )

async def kipoha_question2(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="What language was the Minecraft game created in?",
        reply_markup=await inline_buttons.second_question(),
    )

async def java_answers(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Correctly!",
        reply_markup=await inline_buttons.kipoha_question3(),
    )

async def cpp_answers(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Wrong!",
        reply_markup=await inline_buttons.kipoha_question3(),
    )

async def kipoha_question3(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="What is the name of the founder of the Telegram messenger",
        reply_markup=await inline_buttons.third_question(),
    )

async def pavel_answers(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Correctly!",
    )

async def steve_answers(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Wrong!",
    )


def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(kipoha_question,
                                       lambda call: call.data == "question")
    dp.register_callback_query_handler(disnake_answers,
                                       lambda call: call.data == "disnake")
    dp.register_callback_query_handler(discord_answers,
                                       lambda call: call.data == "discord")
    dp.register_callback_query_handler(kipoha_question2,
                                       lambda call: call.data == "question2")
    dp.register_callback_query_handler(java_answers,
                                       lambda call: call.data == "java")
    dp.register_callback_query_handler(cpp_answers,
                                       lambda call: call.data == "cpp")
    dp.register_callback_query_handler(kipoha_question3,
                                       lambda call: call.data == "question3")
    dp.register_callback_query_handler(pavel_answers,
                                       lambda call: call.data == "pavel")
    dp.register_callback_query_handler(steve_answers,
                                       lambda call: call.data == "steve")



