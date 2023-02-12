import logging
from telegram import MessageEntity
from telegram.ext import Updater, MessageHandler, CommandHandler, PrefixHandler, filters
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def delete_gif(update, context):
    message = update.message
    if message.animation:
        context.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

def main():
    updater = Updater("6239047009:AAGaij2_3bBsYLnNnMFtvyfFG01mOGdswYU")
    handler = MessageHandler(filters.animation, delete_gif)
    updater.dispatcher.add_handler(handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
