from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from app.keyboard import aibtn
from news.run import runews
from news.db import PostDB
import subprocess
import time

rt = Router()

link = ''
text = ''

# user id узнать можно в @userinfobot
@rt.message(F.chat.type == "supergroup", F.from_user.id == "твой user id")
async def start_parse(message: Message):
    if '/start' in message.text:
        a = int(message.text.split(' ')[1])
        await message.delete()
        await message.answer('Погоди ищу новости, можешь пока выйти, ща пришлю')
        await runews(a)
        for i in PostDB().get_items(a):
            try:
                await message.answer(f'{i[0]}\n{i[1]}', reply_markup=aibtn)
            except Exception as ex:
                print(ex)
            time.sleep(3) #задержка для того чтобы ошибок при отправке постов не случалось.

@rt.message(F.chat.type == "supergroup", F.from_user.id == "твой user id")
async def posthand(message: Message): 
    global link, text
    if message.text != '':
        msgtext = message.text
        spl = msgtext.split('\n')
        if len(spl) >= 2: 
            link = spl[0]
            text = spl[1]
            await message.delete()
            await message.answer(text=msgtext, reply_markup=aibtn)

@rt.callback_query(F.data == "llama")
async def calai(callback: CallbackQuery):
    msgtext = callback.message.text
    spl = msgtext.split('\n')
    link = spl[0]
    text = spl[1]
    print(link, text)
    await callback.message.edit_text(f"{link}\n{text}\n------\nЩа, прочитаю....\n------")
    try:
        rrr = subprocess.check_output(["python3", "путь до вашего файла sumtext.py", link]).decode()
        await callback.message.edit_text(f"{link}\n{text}\n{rrr}")
    except Exception:
        await callback.message.answer("Тупит утилитка, попробуй еще!")
    
