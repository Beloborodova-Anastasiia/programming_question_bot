# import logging
import os
# import sys

from dotenv import load_dotenv

load_dotenv()


TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# RETRY_TIME = 600
# HOSTING = 'https://practicum.yandex.ru'
# API_HOMEWORKS = '/api/user_api/homework_statuses/'
# ENDPOINT = HOSTING + API_HOMEWORKS

