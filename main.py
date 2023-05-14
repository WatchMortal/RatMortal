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
