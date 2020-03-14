import os

from aiogram import Bot, Dispatcher, executor, types

from config import API_TOKEN
from .logger import log


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
