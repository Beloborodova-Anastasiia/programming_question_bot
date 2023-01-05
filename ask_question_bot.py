import telegram
from telegram import Bot


TELEGRAM_TOKEN = '5794466732:AAGDZ5-pUAVx9aMeZXGev-uIUMggUdGBL30'
TELEGRAM_CHAT_ID = '5386940741'


def main() -> None:
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    bot.send_message(TELEGRAM_CHAT_ID, 'message')