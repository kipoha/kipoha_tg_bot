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
    survey = InlineKeyboardButton(
        "Survey 💡",
        callback_data="sur"
    )
    my_profile_button = InlineKeyboardButton(
        "Profile 🗒️",
        callback_data="my_profile"
    )
    view_profiles_button = InlineKeyboardButton(
        "View Profiles 🧑🏻‍💻",
        callback_data="view_profiles"
    )
    reference_button = InlineKeyboardButton(
        "Referral Menu 🧐",
        callback_data="reference_menu"
    )
    anecdot_button = InlineKeyboardButton(
        "Random anecdot 😂",
        callback_data="anecdots"
    )
    markup.add(question_button, ban, reg, survey, my_profile_button, view_profiles_button, reference_button, anecdot_button)
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

async def like_dislike_keyboard(owner):
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "Like 👍🏻",
        callback_data=f"like_{owner}"
    )
    dislike_button = InlineKeyboardButton(
        "Dislike 👎🏻",
        callback_data=f"dis_{owner}"
    )
    markup.add(like_button)
    markup.add(dislike_button)
    return markup


async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "Update 💵",
        callback_data=f"update_profile"
    )
    dislike_button = InlineKeyboardButton(
        "Delete ❌",
        callback_data="delete_profile"
    )
    markup.add(like_button)
    markup.add(dislike_button)
    return markup

async def kipoha_rate_button():
    markup = InlineKeyboardMarkup()
    reply = InlineKeyboardButton(
        "Reply",
        callback_data="reply"
    )
    back = InlineKeyboardButton(
        "Back",
        callback_data="back"
    )
    markup.add(reply, back)
    return markup

async def referral_keyboard():
    markup = InlineKeyboardMarkup()
    generate_button = InlineKeyboardButton(
        "Generate Link 🔗",
        callback_data="generate_link"
    )
    list_ref_button = InlineKeyboardButton(
        "Referral list 😎",
        callback_data="list_ref_link"
    )
    balance_button = InlineKeyboardButton(
        "Balance 💳",
        callback_data = "check_bal"
    )
    markup.add(generate_button, list_ref_button, balance_button)
    return markup

async def anecdots_keyboard():
    markup = InlineKeyboardMarkup()
    back = InlineKeyboardButton(
        "Back",
        callback_data="back_to_start"
    )
    anecdot_button = InlineKeyboardButton(
        "Random anecdot 😂",
        callback_data="anecdots"
    )
    markup.add(back, anecdot_button)
    return markup