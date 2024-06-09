from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from MahakRobot import  BOT_USERNAME
from MahakRobot import pbot as app
import requests

EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/Mahakxbot?startgroup=true"),
    ],
]

@app.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text =message.text.split(None, 1)[1]
    m =await message.reply_text( "📝")
    write = requests.get(f"https://apis.xditya.me/write?text={text}").url

    caption = f"""
❖ ᴡʀɪᴛᴛᴇɴ ʙʏ ➥ [˹ ᴍᴀʜᴀᴋ ꭙ ʀᴏʙᴏᴛ™ ♡゙](https://t.me/mahakxbot)
"""
    await m.delete()
    await message.reply_photo(photo=write,caption=caption, reply_markup=InlineKeyboardMarkup(EVAA),)

__mod_name__ = "ᴡʀɪᴛɪɴɢ"

__help__ = """

 ⬤ /write <ᴛᴇxᴛ> *➥* ᴡʀɪᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ.
 """
