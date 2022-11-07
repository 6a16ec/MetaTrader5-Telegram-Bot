import os

from telethon import TelegramClient
from dotenv import load_dotenv
from telethon.events import NewMessage

from helper import Mt5

load_dotenv()
client = TelegramClient('telethon', int(os.environ["TG_API_ID"]), os.environ["TG_API_HASH"])
client.start()
TG_CHANNEL_ID = int(os.environ["TG_CHANNEL_ID"])


@client.on(NewMessage(chats=(TG_CHANNEL_ID,)))
async def channel_handler(event: NewMessage.Event):
    print(event.message.text)
    mt5 = Mt5()
    mt5.set_symbol('GBPJPY')
    mt5.make_order(lot=1, sl=170, tp=165)


client.run_until_disconnected()
