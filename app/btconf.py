import os
from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()
tgtok = os.getenv("TGTOKEN")
bot = Bot(token=tgtok)

