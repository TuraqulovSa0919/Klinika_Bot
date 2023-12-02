from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


til = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🇺🇿O'zbekcha"),
            KeyboardButton("🇷🇺Руский")
        ]
    ],
    resize_keyboard=True
)

contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Raqamni yuborish',\
                           request_contact=True)
        ]
    ],
    resize_keyboard=True
)

kasallik = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Qandli diabet'),
            KeyboardButton('Semizlik')
        ]
    ],
    resize_keyboard=True
)

qandli_tur = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('I tip'),
            KeyboardButton('II tip')
        ],
        [
            KeyboardButton("Bilmayman🤷")
        ]
    ],
    resize_keyboard=True
)

insulin_choice = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Xa"),
            KeyboardButton("Yo'q")
        ]
    ],
    resize_keyboard=True
)

choice_age = ["1 dan 25 yoshgacha", '25 va undan yuqori']

async def yoshi__():
    button = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in choice_age:
        button.add(KeyboardButton(text=i))
    return button


choice_info = ['xa', 'yo\'q']
async def info_():
    button_ = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in choice_info:
        button_.add(KeyboardButton(text=i))
    return button_    