import hashlib

from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from decouple import config
from aiogram.dispatcher.filters import Text
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle


bot = Bot(token=config('TOKEN'))
dp = Dispatcher(bot)


@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    text = query.query or "echo"
    link = 'https://ru.wikipedia.org/wiki/' + text
    result_id: str = hashlib.md5(text.encode()).hexdigest()

    articles = [types.InlineQueryResultArticle(
        id=result_id,
        title='Статья Wikipedia:',
        url=link,
        input_message_content=types.InputTextMessageContent(
            message_text=link
        )
    )]

    await query.answer(articles, cache_time=1, is_personal=True)


executor.start_polling(dp, skip_updates=True)
