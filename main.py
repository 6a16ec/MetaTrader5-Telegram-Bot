import os

from telethon import TelegramClient
from dotenv import load_dotenv
from telethon.events import NewMessage

from helper import Trader

load_dotenv()
client = TelegramClient('telethon', int(os.environ["TG_API_ID"]), os.environ["TG_API_HASH"])
client.start()
TG_CHANNEL_ID = int(os.environ["TG_CHANNEL_ID"])


@client.on(NewMessage(chats=(TG_CHANNEL_ID,)))
async def channel_handler(event: NewMessage.Event):
    print(event.message.text)
    trader = Trader()
    trader.make_order(symbol='GBPJPY', lot=1, sl=170, tp=165)


client.run_until_disconnected()
