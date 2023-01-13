# import telegram
from telegram import Bot
from asyncio import run, Queue
from telegram.ext import Updater
# import requests
from pip._vendor import requests
import gzip
import json
import base64
from typing import Dict, List



from settings import TELEGRAM_CHAT_ID, TELEGRAM_TOKEN
from userstypes import JsonType

HOSTING = 'https://api.stackexchange.com/'
API_SEARCH = '/2.3/search/'
# API_SEARCH = '/2.3/answers'
ENDPOINT = HOSTING + API_SEARCH
PARAMS = {
    'site': 'stackoverflow',
    'order': 'desc',
    'sort': 'activity',
    'intitle': 'pandas',
    'tagget': 'python'
}
HEADERS = {}


def get_api_answer_items(endpoint: str, headers: Dict, params: Dict) -> List:
    request = requests.get(
            endpoint, headers=headers, params=params
        )
    if type(request.content) is bytes:
        decode_content = json.loads(request.text)
    return decode_content['items']


async def main() -> None:
    bot = Bot(token=TELEGRAM_TOKEN)
    await bot.initialize()
    queue = Queue(maxsize=10)
    updater = Updater(bot, queue) 

    async with updater:
        await updater.start_polling(poll_interval=2)
        while True:
            update = await queue.get()
            message = update.message.text
            queue.task_done()
            # await bot.send_message(TELEGRAM_CHAT_ID, message)
            PARAMS['intitle'] = message

            items = get_api_answer_items(ENDPOINT, HEADERS, PARAMS)
            for item in items:
                print(item['title'])
    

if __name__ == '__main__':
    run(main())
