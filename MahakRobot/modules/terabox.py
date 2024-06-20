import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater,  MessageHandler, Filters
from MahakRobot import TOKEN 
from MahakRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, CommandHandler, 
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

                # Shorten links using TinyURL API
                tinyurl_api = "http://tinyurl.com/api-create.php?url="
                shortened_fast_download_link = requests.get(tinyurl_api + fast_download_link).text
                shortened_hd_video_link = requests.get(tinyurl_api + hd_video_link).text

                # Create inline keyboard markup
                reply_markup = InlineKeyboardMarkup([
                    [
                        InlineKeyboardButton(text='➡️ Fast Download', url=shortened_fast_download_link),
                        InlineKeyboardButton(text='▶️ HD Video', url=shortened_hd_video_link)
                    ],
                    [
                        InlineKeyboardButton(text='Developer', url='https://t.me/itz_Asuraa')
                    ]
                ])

                message_text = f"🎬 <b>Title:</b> {video_title}\nMade with ❤️ by @itz_Asuraa"

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
                    text="❌ <b>Error fetching data from Terabox API</b>",
                    parse_mode="HTML"
                )
        except Exception as e:
            context.bot.send_message(
                chat_id=chat_id,
                text=f"❌ <b>Error: {str(e)}</b>",
                parse_mode="HTML"
            )
    else:
        context.bot.send_message(
            chat_id=chat_id,
            text="ℹ️ Please provide a valid URL after /info command."
        )

# Command handler registration
dispatcher.add_handler(CommandHandler("terabox", handle_terabox_command, run_async=True))

updater.start_polling()
updater.idle()
