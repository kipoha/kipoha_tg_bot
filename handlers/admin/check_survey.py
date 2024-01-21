from aiogram import types, Dispatcher
from config import bot
from database import databases
from keyboards import inline_buttons
from config import bot, MEDIA_DESTINATION, GROUP_ID
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from const import PROFILE_TEXT


async def check_admin(message: types.Message):
    chat_member = await bot.get_chat_member(GROUP_ID, message.from_user.id)
    return chat_member.status in ['administrator', 'creator']

class CheckSurvey(StatesGroup):
    check_survey = State()

async def check_survey(message: types.Message):
    admin = await check_admin(message)
    db = databases.DataBase()
    surveys = db.kipoha_get_survey()
    if admin:
        text = ''
        for survey in surveys:
            text += f'{survey[0]}. {survey[1]}\n'
        await bot.send_message(
            chat_id=message.from_user.id,
            text=text + '\nchoose a survey you want to'
        )
        print(admin)
        await CheckSurvey.check_survey.set()
    else:
        print(admin)
        return

async def load_numb_survey(message: types.Message, state: FSMContext):
    db = databases.DataBase()
    try:
        type(int(message.text))
    except ValueError:
        await bot.send_message(
            chat_id=message.from_user.id,
            text='ONLY numeric text\n'
        )
        await state.finish()
        return
    async with state.proxy() as data:
        data['check_survey'] = message.text
        print(data)
    try:
        survey = db.kipoha_select_survey(data['check_survey'])
        mention = f'[User](tg://user?id={survey[3]})'
        text = f'Idea: {survey[1]}\nProblem: {survey[2]}\nUser: {mention}'
    except TypeError:
        text = f'is not found'
    await bot.send_message(
        chat_id=message.from_user.id,
        text=text,
        parse_mode="MarkdownV2",
        reply_markup=await inline_buttons.kipoha_rate_button()
    )
    await state.finish()

async def send_rate(message: types.Message, state: FSMContext):
    db = databases.DataBase()
    async with state.proxy() as data:
        user = db.kipoha_select_survey(data['check_survey'])
    try:
        await bot.send_message(
            chat_id=user[3],
            text='idk'
        )
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f'Idea'
        )
    except:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f'no'
        )

def reg_adm_survey_handlers(dp: Dispatcher):
    dp.register_message_handler(
        check_survey,
        commands=['check_adm_survey']
    )
    dp.register_callback_query_handler(
        check_survey,
        lambda call: call.data == 'back'
    )
    dp.register_callback_query_handler(
        send_rate,
        lambda call: call.data == 'reply'
    )
    dp.register_message_handler(
        load_numb_survey,
        state=CheckSurvey.check_survey,
        content_types=['text']
    )

