
from instrgemini import main as instr
import asyncio
from askgemini import askbot
import os
from dotenv import load_dotenv
from checkgemini import main as testgemini
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)
from sphere_gemini import main as sphere_main


load_dotenv()

TELEGRAM_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

USER_STATE = {}
PICK_STATES = {}
CHECK_STATES = {}

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Eco market leaders! 🌿"),
        ],
        [
            KeyboardButton(text="Environmentally friendly industries 🌍"),
        ],
        [
            KeyboardButton(text="Eco-tools 🛠"),
        ],
    ],
    resize_keyboard=True,
)


@dp.message_handler(commands=["start"])
async def handle_start(message: types.Message):
    USER_STATE[message.from_user.id] = ""
    PICK_STATES[message.from_user.id] = 0
    CHECK_STATES[message.from_user.id] = 0
    welcome_msg = """ 
🌟 Welcome to a world of possibilities with Ecosystems AI! 🌍

Are you eager to contribute to sustainable development and explore new horizons? Looking for ways to make your lifestyle more eco-friendly and conscious? We are here to inspire and support you every step of the way on this exciting journey!

✨ What Ecosystems AI does for you:

🌱 Ecological Consciousness: Our artificial intelligence analyzes environmental data every day, helping you understand how your actions can contribute to its preservation.

🔎 Informed: Get up-to-date information and knowledge based on reliable research and data about the state of the planet and how to protect it.

📚 Training and Tips: Explore new sustainability methods and practices, get educational materials and tips from environmental and sustainability experts.

🔄 Up-to-date: We continuously update information to keep you up-to-date with the latest research and news in ecology and sustainability.

🌟 Join Ecosystems AI now and together we'll make the world a better place!

🌍 Let yourself be part of global change with Ecosystems AI! 🌟 
 """
    await bot.send_message(message.chat.id, welcome_msg , reply_markup=keyboard)
    
@dp.message_handler(commands=['ask'])
async def askgpt(message: types.Message):
    loading_message = await message.reply("Загрузка...")
    response = askbot(message.text)
    await asyncio.sleep(2)

    await bot.edit_message_text(
    text=response,
    chat_id=loading_message.chat.id,
    message_id=loading_message.message_id,
)

@dp.message_handler(
    lambda message: message.text == "Eco market leaders! 🌿"
)
async def handle_test_gemini(message: types.Message):
    loading_message = await message.reply("Загрузка...")
    response = testgemini()
    await asyncio.sleep(2)

    await bot.edit_message_text(
        response, chat_id=loading_message.chat.id, message_id=loading_message.message_id
    )

@dp.message_handler(
    lambda message: message.text == "Environmentally friendly industries 🌍"
)
async def handle_test_gpt(message: types.Message):
    loading_message = await message.reply("Загрузка...")
    response = sphere_main()
    await asyncio.sleep(2)

    await bot.edit_message_text(
        response, chat_id=loading_message.chat.id, message_id=loading_message.message_id
    )

@dp.message_handler(
    lambda message: message.text == "Eco-tools 🛠"
)
async def handle_test_gemini(message: types.Message):
    loading_message = await message.reply("Загрузка...")
    response = instr()
    await asyncio.sleep(2)

    await bot.edit_message_text(
        response, chat_id=loading_message.chat.id, message_id=loading_message.message_id
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
