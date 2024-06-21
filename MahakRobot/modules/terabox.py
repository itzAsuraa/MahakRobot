import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater,  MessageHandler, Filters
from MahakRobot import TOKEN 
from MahakRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, CommandHandler
from MahakRobot import dispatcher

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Handler for /terabox <URL> command
def handle_terabox_command(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    command_parts = update.message.text.split(maxsplit=1)

    if len(command_parts) == 2:
        url = command_parts[1]

        try:
            response = requests.get(f"https://teraboxvideodownloader.nepcoderdevs.workers.dev/?url={url}")
            if response.status_code == 200:
                data = response.json()
                resolutions = data["response"][0]["resolutions"]
                fast_download_link = resolutions.get("Fast Download")
                hd_video_link = resolutions.get("HD Video")
                thumbnail_url = data["response"][0]["thumbnail"]
                video_title = data["response"][0]["title"]

                if not fast_download_link or not hd_video_link:
                    raise Exception("Download links not found.")

                # Create inline keyboard markup
                reply_markup = InlineKeyboardMarkup([
                    [
                        InlineKeyboardButton(text= ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ', url=fast_download_link),
                    [
                        InlineKeyboardButton(text='ᴏᴡɴᴇʀ', url='https://t.me/itz_Asuraa')
                    ]
                ])

                message_text = f"🎬 <b>Title:</b> {video_title}"

                context.bot.send_photo(
                    chat_id=chat_id,
                    photo=thumbnail_url,
                    caption=message_text,
                    parse_mode="HTML",
                    reply_markup=reply_markup
                )
            else:
                context.bot.send_message(
                    chat_id=chat_id,
                    text=" <b>Error fetching data from Terabox API</b>",
                    parse_mode="HTML"
                )
        except Exception as e:
            context.bot.send_message(
                chat_id=chat_id,
                text=f" <b>Error: {str(e)}</b>",
                parse_mode="HTML"
            )
    else:
        context.bot.send_message(
            chat_id=chat_id,
            text="Please provide a valid URL after /terabox command."
        )

# Command handler registration
dispatcher.add_handler(CommandHandler("terabox", handle_terabox_command, run_async=True))

updater.start_polling()
updater.idle()
