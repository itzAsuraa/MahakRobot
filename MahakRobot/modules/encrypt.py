import secureme
from pyrogram import filters
from Mahakxbot import pbot as avisha


@avisha.on_message(filters.command("encrypt"))
async def encyrpt(bot, message):
    if len(message.command) < 2:
        return await message.reply_text("**⬤ ᴇxᴀᴍᴘʟᴇ ➥ /encyrpt ɪɴᴅɪᴀ")
    m = message.text.split(' ',1)[1]
    try:
        Secure = secureme.encrypt(m)
        
        await message.reply_text(f"`{Secure}`")
        

    except Exception as e:
        await message.reply_text(f"⬤ Error ➥ {e}")

@avisha.on_message(filters.command("decrypt"))
async def decrypt(bot, message):
    if len(message.command) < 2:
        return await message.reply_text("**⬤ ᴇxᴀᴍᴘʟᴇ ➥ /decrypt ɴsɪɴғ")
    m = message.text.split(' ',1)[1]
    try:
        Decrypt = secureme.decrypt(m)
        
        await message.reply_text(f"`{Decrypt}`")
        

    except Exception as e:
        await message.reply_text(f"{e}")


__mod_name__ = "ᴇɴᴄʀʏᴘᴛ"

__help__ = """

 ⬤ /encrypt* ➥* ᴇɴᴄʀʏᴘᴛs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ
 ⬤ /decrypt* ➥* ᴅᴇᴄʀʏᴘᴛs ᴘʀᴇᴠɪᴏᴜsʟʏ ᴇᴄʀʏᴘᴛᴇᴅ ᴛᴇxᴛ
 ⬤ /uselessfact *➥* ɢᴇɴᴇʀᴀᴛᴇ  ʀᴀᴍᴅᴏᴍ ᴜsᴇʟᴇss ғᴀᴄᴛ
"""
