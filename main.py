import os

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

from order import Order
from trader import make_order

load_dotenv()
bot = Bot(token=os.getenv('TG_BOT_TOKEN'))
dp = Dispatcher(bot)
USER_ID = int(os.getenv('TG_USER_ID'))


@dp.message_handler()
async def base_handler(message: types.Message):
    if message.chat.id == USER_ID:
        order = Order(message.text)
        if order.is_valid():
            await message.reply('Order found')
            make_order(order)
            await message.reply('Order is made')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)