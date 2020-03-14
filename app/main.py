import os

from aiogram import Bot, Dispatcher, executor, types

from config import API_TOKEN
from .logger import log


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """This handler will be called when user sends `/start` or `/help` command"""
    await message.reply("Hi!\nI'm a Bot!\nPowered by aiogram.")
