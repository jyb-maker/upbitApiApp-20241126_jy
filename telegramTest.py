# pip install python-telegram-bot

import telegram
import asyncio

bot = telegram.Bot(token="7255077661:AAHxpM1icq2Xkg8wzkASo0JbTxh3e67tl6E") # 텔레그램 api-key값
chat_id = "7868775703"

asyncio.run(bot.sendMessage(chat_id=chat_id, text="파이썬 텔레그램 테스트!"))























