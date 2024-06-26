import logging
import os
import platform
import psutil
import time

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message
from MahakRobot import BOT_USERNAME, OWNER_ID
from MahakRobot import pbot as app

# Configure logging
logging.basicConfig(level=logging.INFO)

# Constants
FORBIDDEN_KEYWORDS = [
    "porn", "xxx", "NCERT", "ncert", "ans", "Pre-Medical",
    "kinematics", "Experiment", "experiments", "Ans", "jee",
    "Allen", "pre-medical", "institute"
]

# Handle Forbidden Keywords
@app.on_message(filters.text & filters.group)
async def handle_forbidden_keywords(_, message):
    if any(keyword.lower() in message.text.lower() for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.message_id} containing forbidden keywords")
        await message.delete()
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")
    elif message.caption and any(keyword.lower() in message.caption.lower() for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.message_id} containing forbidden keywords in caption")
        await message.delete()
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")

# Delete long edited messages but keep short messages and emoji reactions
async def delete_long_edited_messages(client, edited_message: Message):
    if edited_message.text and len(edited_message.text.split()) > 15:
        logging.info(f"Deleting long edited message with ID {edited_message.message_id}")
        await edited_message.delete()
    elif edited_message.sticker or edited_message.animation:
        logging.info(f"Keeping sticker or animation edited message with ID {edited_message.message_id}")
        return

@app.on_edited_message(filters.group & ~filters.me)
async def handle_edited_messages(_, edited_message: Message):
    await delete_long_edited_messages(_, edited_message)

# Delete long messages in groups and reply with a warning
MAX_MESSAGE_LENGTH = 50  # Define the maximum allowed length for a message

async def delete_long_messages(client, message: Message):
    if message.text and len(message.text.split()) > MAX_MESSAGE_LENGTH:
        logging.info(f"Deleting long message with ID {message.message_id}")
        await message.delete()

@app.on_message(filters.group & ~filters.me)
async def handle_messages(_, message: Message):
    await delete_long_messages(_, message)
