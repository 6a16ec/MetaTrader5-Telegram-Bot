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
            await message.reply('Order found', reply=False)
            result1 = make_order(order, tp_number=1)
            result2 = make_order(order, tp_number=2)
            if result1 and result2:
                await message.reply('Request executed successfully', reply=False)
            else:
                await message.reply('Problem when executing a request', reply=False)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)