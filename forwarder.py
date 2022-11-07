import os

from telethon import TelegramClient
from dotenv import load_dotenv
from telethon.events import NewMessage

from helper import Trader

load_dotenv()
client = TelegramClient('telethon', int(os.environ["TG_API_ID"]), os.environ["TG_API_HASH"])
client.start()
TG_CHANNEL_ID = int(os.environ["TG_CHANNEL_ID"])
BOT_USERNAME = int(os.environ["BOT_USERNAME"])


@client.on(NewMessage(chats=(TG_CHANNEL_ID,)))
async def channel_handler(event: NewMessage.Event):
    await client.send_message(BOT_USERNAME, event.message.text)


client.run_until_disconnected()