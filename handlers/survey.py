from aiogram import types, Dispatcher
from config import bot
from database import databases
from keyboards import inline_buttons
from config import bot, MEDIA_DESTINATION
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from const import PROFILE_TEXT

class SurveyStates(StatesGroup):
    idea = State()
    problems = State()

async def survey_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Send me ur idea for bot'
    )
    await SurveyStates.idea.set()

async def load_idea(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['idea'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='What problems have u encountered?'
    )

    await SurveyStates.next()

async def load_problem(message: types.Message, state: FSMContext):
    db = databases.DataBase()
    async with state.proxy() as data:
        data['problem'] = message.text
        print(data)

    async with state.proxy() as data:
        db.kipoha_add_survey(
            tg_id=message.from_user.id,
            idea=data['idea'],
            propblem=data['problem'],
        )

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Thank u for survey'
    )
    await state.finish()

def reg_survey_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        survey_start,
        lambda call: call.data == "sur"
    )
    dp.register_message_handler(
        load_idea,
        state=SurveyStates.idea,
        content_types=['text']
    ),
    dp.register_message_handler(
        load_problem,
        state=SurveyStates.problems,
        content_types=['text']
    )