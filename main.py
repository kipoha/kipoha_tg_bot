from aiogram import executor
from config import dp
from handlers import (
    start,
    questionnaire,
    chat_actions,
    check_ban,
    registration,
    # update_profile,
    survey,
    profile
)
from handlers.admin import (
    check_survey
)
from database import databases


async def on_startup(_):
    db = databases.DataBase()
    db.kipoha_create_table()


start.reg_kipoha_start_handlers(dp=dp)
questionnaire.reg_questionnaire_handlers(dp=dp)
check_ban.reg_bans_handlers(dp=dp)
registration.reg_registration_handlers(dp=dp)
# update_profile.reg_update_profile_handlers(dp=dp)
survey.reg_survey_handlers(dp=dp)
check_survey.reg_adm_survey_handlers(dp=dp)
profile.reg_profile_handlers(dp=dp)
chat_actions.reg_chat_actions_handlers(dp=dp)

if __name__ == "__main__":
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup
    )
