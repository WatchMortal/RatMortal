from telegram.ext import Updater

def start_command(update, context):

  message = "Merhaba ben Emre , Hoşgeldin"

  

  return update.message.reply_text(message)
