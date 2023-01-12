# import telegram
from telegram import Bot
from asyncio import run, Queue
from telegram.ext import Updater, MessageHandler

from settings import TELEGRAM_CHAT_ID, TELEGRAM_TOKEN


async def main() -> None:
    bot = Bot(token=TELEGRAM_TOKEN)
    message = 'Hi'
    await bot.initialize()
    queue = Queue(maxsize=10)
    updater = Updater(bot, queue) 
    async with updater:
        await updater.start_polling(poll_interval=2)
        while True:
            update = await queue.get()
            message = update.message.text
            queue.task_done()
            await bot.send_message(TELEGRAM_CHAT_ID, message)
            print(message)
    # try:
    #     await updater.initialize()
    #     await updater.start_polling(poll_interval=2)
    #     while True:
    #         update = await queue.get()
    #         message = update.message.text
    #         queue.task_done()
    #         await bot.send_message(TELEGRAM_CHAT_ID, message)
    #         print(message)
    #         if queue.full():
    #             break

    # finally:
    #     print(queue)
    #     await updater.stop()
    #     await updater.shutdown()

if __name__ == '__main__':
    run(main())
