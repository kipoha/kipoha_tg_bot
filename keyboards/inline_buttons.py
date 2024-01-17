from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


async def kipoha_start_keyboard():
    markup = InlineKeyboardMarkup()
    question_button = InlineKeyboardButton(
        "Question 🤔",
        callback_data="question"
    )
    ban = InlineKeyboardButton(
        "Check ban user 💢",
        callback_data="bans"
    )
    reg = InlineKeyboardButton(
        "Registration ✅",
        callback_data="reg"
    )
    markup.add(question_button)
    markup.add(ban)
    markup.add(reg)
    return markup


async def first_question():
    markup = InlineKeyboardMarkup()
    disnake = InlineKeyboardButton(
        "Disnake 👍",
        callback_data="disnake"
    )
    discord = InlineKeyboardButton(
        "Discord 👴",
        callback_data="discord"
    )
    markup.add(disnake)
    markup.add(discord)
    return markup

async def kipoha_question2():
    markup = InlineKeyboardMarkup()
    question_button = InlineKeyboardButton(
        "Question2 🤔",
        callback_data="question2"
    )
    markup.add(question_button)
    return markup

async def second_question():
    markup = InlineKeyboardMarkup()
    java = InlineKeyboardButton(
        "Java 🍵",
        callback_data="java"
    )
    cpp = InlineKeyboardButton(
        "C++ ➕",
        callback_data="cpp"
    )
    markup.add(java)
    markup.add(cpp)
    return markup

async def kipoha_question3():
    markup = InlineKeyboardMarkup()
    question_button = InlineKeyboardButton(
        "Question3 🤔",
        callback_data="question3"
    )
    markup.add(question_button)
    return markup

async def third_question():
    markup = InlineKeyboardMarkup()
    pavel = InlineKeyboardButton(
        "Pavel Dyrov",
        callback_data="pavel"
    )
    steve = InlineKeyboardButton(
        "Steve Jobs",
        callback_data="steve"
    )
    markup.add(pavel)
    markup.add(steve)
    return markup

async def kipoha_update_profile_button():
    markup = InlineKeyboardMarkup()
    pr_button = InlineKeyboardButton(
        "Update Profile 🔁",
        callback_data="pr_update"
    )
    markup.add(pr_button)
    return markup

async def kipoha_select_profile_button():
    markup = InlineKeyboardMarkup()
    nick = InlineKeyboardButton(
        "Nickname 👤",
        callback_data="nick"
    )
    bio = InlineKeyboardButton(
        "Biography 👥",
        callback_data="bio"
    )
    age = InlineKeyboardButton(
        "Age 🕐",
        callback_data="age"
    )
    sign = InlineKeyboardButton(
        "Zodiac Sign ❓",
        callback_data="sign"
    )
    f_game = InlineKeyboardButton(
        "Favorite games 🎮",
        callback_data="f_game"
    )
    country = InlineKeyboardButton(
        "Country 🌐",
        callback_data="country"
    )
    photo = InlineKeyboardButton(
        "Photo 📷",
        callback_data="photo"
    )
    markup.add(nick, bio, age, sign, f_game, country, photo)
    return markup