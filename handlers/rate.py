from aiogram import types, Dispatcher
from config import bot
from database import databases
from keyboards import inline_buttons
from config import bot, MEDIA_DESTINATION, GROUP_ID
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from const import PROFILE_TEXT


class RateStates(StatesGroup):
    rate = State()

async def start_rate(call: types.CallbackQuery, state: FSMContext):
    pass