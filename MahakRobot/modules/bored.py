from pyrogram import Client, filters
import requests
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from MahakRobot import pbot as app


EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/mahakxbot?startgroup=true"),
    ],
]


bored_api_url = "https://apis.scrimba.com/bored/api/activity"

@app.on_message(filters.command("bored", prefixes="/"))
async def bored_command(client, message):
    # Fetch a random activity from the Bored API
    response = requests.get(bored_api_url)
    if response.status_code == 200:
        data = response.json()
        activity = data.get("activity")
        if activity:
            
            await message.reply(f"❖ ғᴇᴇʟɪɴɢ ʙᴏʀᴇᴅ ? ʜᴏᴡ ᴀʙᴏᴜᴛ ⏤͟͟͞͞★\n\n❅ `{activity}`\n\n❖ ғᴇᴇʟɪɴɢ ʙʏ ➥ [˹ᴍᴀʜᴀᴋ ꭙ ʀᴏʙᴏᴛ™ ♡゙](@MahakXbot)", reply_markup=InlineKeyboardMarkup(EVAA),)
        else:
            await message.reply("⬤ ɴᴏ ᴀᴄᴛɪᴠɪᴛʏ ғᴏᴜɴᴅ.")
    else:
        await message.reply("⬤ ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ᴀᴄᴛɪᴠɪᴛʏ.")


__help__ = """
⬤ /bored ➥ ɢᴇᴛ ʀᴀɴᴅᴏᴍ ʙᴏʀᴇᴅ ғᴇᴇʟɪɴɢs.
"""

__mod_name__ = "ʙᴏʀᴇᴅ"
