from pyromod import listen
from pyrogram import *
from os import system as run
import asyncio
from io import BytesIO
from pyrogram.types import Message
import time
from main import *

ME = "5352056779"

app = Client(
    "bot",
    bot_token="5595433257:AAFw4gle8efQgWWiOTM_cPiQsZMfUXg5Q3Q",
    api_id="3401428",
    api_hash="4df0fcad01a1c5aec6c8b72c26302194",
)


pesan = """
Hi, i am UptimerRobot, monitoring your website.

**commands list:**
- /add : create new monitor
- /del : delete the monitor
"""


@app.on_message(filters.command("start"))
async def on(app, msg):
    await msg.reply_text(f"{pesan}")


@app.on_message(filters.command("add"))
async def add(app, msg):
    chat_id = int(msg.chat.id)
    nama = await app.ask(chat_id, "send name:")
    domain = await app.ask(chat_id, "send domain:")
    a = nama.text
    b = domain.text
    hasil = new(a,b)
    await msg.reply_text(hasil)



@app.on_message(filters.command("del"))
async def dele(app, msg):
    chat_id = int(msg.chat.id)
    nama = await app.ask(chat_id, "send monitor id:")
    a = nama.text
    hasil = hapus(a)
    #await msg.reply_text("succeed !")
    await msg.reply_text(hasil)



print("bot aktif !")
app.run()
