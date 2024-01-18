from aiogram import types, Dispatcher
from config import bot
from database import databases
from keyboards import inline_buttons
from config import bot, MEDIA_DESTINATION
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from const import PROFILE_TEXT

class RegistrationStates(StatesGroup):
    nickname = State()
    bio = State()
    age = State()
    zodiac_sigh = State()
    games = State()
    country = State()
    photo = State()

async def reg_start(call: types.CallbackQuery):
    db = databases.DataBase()
    pr = db.kipoha_select_profile(call.from_user.id)
    if pr:
        await bot.send_message(
            chat_id=call.from_user.id,
            text='U r already registered'
            # text='U r already registered, to update ur profile, click on the button below',
            # reply_markup=await inline_buttons.kipoha_update_profile_button()
        )
        return
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Send me ur Nickname, please!'
    )
    await RegistrationStates.nickname.set()

async def load_nickname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Send me ur Bio!'
    )
    await RegistrationStates.next()

async def load_bio(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['bio'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='How old r u ?\n'
             '(Only numeric age in text)\n'
             'Example: 27, 28'
    )
    await RegistrationStates.next()

async def load_age(message: types.Message,
                   state: FSMContext):
    try:
        type(int(message.text))
    except ValueError:
        await bot.send_message(
            chat_id=message.from_user.id,
            text='I told u send me ONLY numeric text\n'
                 'registration failed ❌\n'
                 'Restart registration!!!'
        )
        await state.finish()
        return

    async with state.proxy() as data:
        data['age'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='What is ur Zodiac Sign ?'
    )

    await RegistrationStates.next()

async def load_zodiac(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['sign'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Write ur favorite games'
    )
    await RegistrationStates.next()

async def load_games(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['games'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='What country do u live in?'
    )
    await RegistrationStates.next()

async def load_country(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['country'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Send me ur photo\n'
             '(only in photo mode sender)'
    )
    await RegistrationStates.next()

async def load_photo(message: types.Message, state: FSMContext):
    db = databases.DataBase()
    path = await message.photo[-1].download(
        destination_dir=MEDIA_DESTINATION
    )
    async with state.proxy() as data:
        db.kipoha_add_profile(
            tg_id=message.from_user.id,
            nickname=data['nickname'],
            bio=data['bio'],
            age=data['age'],
            sign=data['sign'],
            games=data['games'],
            country=data['country'],
            photo=path.name,
        )

    with open(path.name, 'rb') as photo:
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=photo,
            caption=PROFILE_TEXT.format(
                nickname=data['nickname'],
                bio=data['bio'],
                age=data['age'],
                sign=data['sign'],
                games=data['games'],
                country=data['country'],
            ),
        )
    await bot.send_message(
        chat_id=message.from_user.id,
        text='U have successfully Registered'
    )
    await state.finish()



def reg_registration_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        reg_start,
        lambda call: call.data == "reg"
    )
    dp.register_message_handler(
        load_nickname,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_bio,
        state=RegistrationStates.bio,
        content_types=['text']
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=['text']
    )
    dp.register_message_handler(
        load_zodiac,
        state=RegistrationStates.zodiac_sigh,
        content_types=['text']
    ),
    dp.register_message_handler(
        load_games,
        state=RegistrationStates.games,
        content_types=['text']
    )
    dp.register_message_handler(
        load_country,
        state=RegistrationStates.country,
        content_types=['text']
    )
    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=types.ContentTypes.PHOTO
    )
