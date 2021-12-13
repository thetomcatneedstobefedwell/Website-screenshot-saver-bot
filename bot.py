import os
import logging
import validators
from config import *
from selenium import webdriver
from aiogram.types import InputFile
from Screenshot import Screenshot_Clipping
from aiogram import Bot, Dispatcher, executor, types

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm Telegram Bot!\nI can make a screenshot of a webpage for you. Please send me a link.")

@dp.message_handler()
async def echo(message: types.Message):

    if validators.url(message.text):
        await message.reply("Start working. It may take a while. Please wait.")
        takeScreenshot(message.text)
        file = InputFile('screen.png')
        await bot.send_photo(message.from_user.id, file)
        os.remove('screen.png')
    else:
        await message.reply("Link is invalid. Please provide a valid one.")

def takeScreenshot(url):
    ss = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    driver.maximize_window()
    driver.get(url)
    image = ss.full_Screenshot(driver, save_path=r'.' , image_name='screen.png')

if name == 'main':
    executor.start_polling(dp, skip_updates=True)
