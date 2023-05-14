from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "6248001249:AAFNdpxbJr1DZoEiDVB8_gpb0hCHfayCL34"

print("Bot çalışmaya başladı!")

def main():

    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    updater.start_polling()

    updater.idle()

if __name__ == "__main__":

    main()


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import commands as c

TOKEN = "1685639520:AAHf0jD739qNURYHedUZSlYx-3GCrX91ts8"

print("Bot çalışmaya başladı!")

def main():

    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    #start komutu

    dp.add_handler(CommandHandler("start", c.start_command))

    # tanımsız bir mesaj girildiğinde

    dp.add_handler(MessageHandler(Filters.text, c.wrong_command))

    updater.start_polling()

    updater.idle()

if __name__ == "__main__":

    main()
