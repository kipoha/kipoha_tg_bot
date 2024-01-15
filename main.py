from aiogram import executor
from config import dp
from handlers import (
    start,
    questionnaire,
    chat_actions,
    check_ban,
)
from database import databases


async def on_startup(_):
    db = databases.DataBase()
    db.kipoha_create_table()


start.reg_kipoha_start_handlers(dp=dp)
questionnaire.register_questionnaire_handlers(dp=dp)
chat_actions.reg_chat_actions_handlers(dp=dp)
check_ban.register_bans_handlers(dp=dp)

if __name__ == "__main__":
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup
    )
