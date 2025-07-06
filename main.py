import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types.web_app_info import WebAppInfo


TOKEN = '7956348743:AAF3jabsjn_dR2AaN_La2hk9Mb1gekP6u-w'

dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: types.Message):

    button = types.KeyboardButton(
        text='Open web',
        web_app=WebAppInfo(url='https://itproger.com/course/telegram-bot/8'))

    markup = types.ReplyKeyboardMarkup(
        keyboard=[[button]],
        resize_keyboard=True)

    await message.answer(
        text='Hello, my frends...',
        reply_markup=markup)


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
