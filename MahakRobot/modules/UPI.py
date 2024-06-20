import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater,  MessageHandler, Filters
from MahakRobot import TOKEN 
from MahakRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, CommandHandler
from MahakRobot import dispatcher



updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Function to validate VPA
def validate_vpa(update: Update, context: CallbackContext):
    vpa = context.args[0] if context.args else None
    if not vpa:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please provide a VPA.")
        return

    url = f"https://paydigi.airtel.in/web/pg-service/v1/validate/vpa/{vpa}"
    response = requests.get(url)

    if response.status_code == 200:
        context.bot.send_message(chat_id=update.effective_chat.id, text="UPI is valid")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="UPI is not valid")
        context.bot.send_message(chat_id=update.effective_chat.id, text=response.text)

# Command handler registration
dispatcher.add_handler(CommandHandler("validatevpa", validate_vpa))

# Start the bot
updater.start_polling()
updater.idle()
