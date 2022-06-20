import telegram
from telegram.ext import Updater, MessageHandler, Filters

token = "5086663851:AAHBTMK-EXP5QaEKaPIJNJ9_o-4zTV74xwE"
chat_id = "5093226994"

telegram_bot = telegram.Bot(token=token)
telegram_bot.sendMessage(chat_id=chat_id, text="자동 알람 메시지입니다!")

updater = Updater(token=token, use_context=True)
dispather = updater.dispatcher
updater.start_polling()

def handler(update, context):
    user_text = update.message.text
    if user_text == "1":
        telegram_bot.sendMessage(chat_id=chat_id, text="1이 입력되었습니다.")
    elif user_text == "2":
        telegram_bot.sendMessage(chat_id=chat_id, text="2가 입력되었습니다.")

echo_handler = MessageHandler(Filters.text, handler)
dispather.add_handler(echo_handler)


