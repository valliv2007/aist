import os
import telegram
from dotenv import load_dotenv


load_dotenv()

TELEGRAM_TOKEN = str(os.getenv('TOKEN_BOT'))
TELEGRAM_CHAT_ID = os.getenv('PHONE_ID')


def send_telegram(message):
    """Отправка сообщения ботом."""
    try:
        bot = telegram.Bot(TELEGRAM_TOKEN)
        bot.send_message(TELEGRAM_CHAT_ID, message)
    except telegram.error.TelegramError as error:
        print(error)
