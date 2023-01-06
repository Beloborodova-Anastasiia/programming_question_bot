# import telegram
from telegram import Bot
from asyncio import run

from settings import TELEGRAM_CHAT_ID, TELEGRAM_TOKEN


async def main() -> None:
    bot = Bot(token=TELEGRAM_TOKEN)
    message = 'Hi'
    await bot.send_message(TELEGRAM_CHAT_ID, message)


if __name__ == '__main__':
    run(main())
