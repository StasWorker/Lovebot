from telegram import Bot
from apscheduler.schedulers.blocking import BlockingScheduler
import asyncio

TOKEN = "8885787471:AAHq_beNXwV3FF2OsZvWqXCGgsdh2HqmSXs"
CHAT_ID = 1173742740

async def send_message():
    bot = Bot(token=TOKEN)
    await bot.send_message(
        chat_id=CHAT_ID,
        text="❤️ Я люблю тебя очень сильно ❤️"
    )

def job():
    asyncio.run(send_message())

scheduler = BlockingScheduler()

# Каждый день в 09:00
scheduler.add_job(job, "cron", hour=9, minute=0)

print("Бот запущен!")
job()  # Отправит сообщение сразу после запуска (для проверки)
scheduler.start()