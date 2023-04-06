from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from decouple import config


bot = Bot(token=config('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await message.reply('Приует!!!')


@dp.message_handler(commands=['команда'])
async def echo(message: types.Message):
    await message.answer(message.text)


# @dp.message_handler(lambda message: 'такси' in message.text)
# async def taxi(message: types.Message):
#     await message.answer('такси')


@dp.message_handler(lambda message: 'нло' in message.text)
async def ufo(message: types.Message):
    await message.answer('нло')


@dp.message_handler(lambda message: message.text.startswith('такси'))
async def ufo(message: types.Message):
    await message.answer(message.text[6:])


@dp.message_handler()
async def empty(message: types.Message):
    await message.answer('Нет такой команды')
    await message.delete()

executor.start_polling(dp, skip_updates=True)
