import logging
from typing import Text

from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup
from settings import TG_TOKEN
import requests

API_TOKEN = TG_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    print('Кто-то написал!')
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler(commands=['anecdote'])
async def get_anecdote(message: types.Message):
    receive = requests.get('http://anekdotme.ru/random')
    page = BeautifulSoup(receive.text, 'html.parser')
    find = page.select('.anekdot_text')
    for text in find:
        page = (text.getText().strip())
    await message.reply(page)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
