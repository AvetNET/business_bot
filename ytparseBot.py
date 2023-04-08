import hashlib

from youtube_search import YoutubeSearch
from aiogram import Bot, types, utils
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from decouple import config


def searcher(text):
    res = YoutubeSearch(text, max_results=5).to_dict()
    return res


bot = Bot(token=config('TOKEN'))
dp = Dispatcher(bot)


@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    text = query.query or 'echo'
    links = searcher(text)

    articles = [types.InlineQueryResultArticle(
        id=hashlib.md5(f'{link["id"]}'.encode()).hexdigest(),
        title=f'{link["title"]}',
        url=f'https://www.youtube.com/watch?v={link["id"]}',
        thumb_url=f'{link["thumbnails"][0]}',
        input_message_content=types.InputTextMessageContent(
            message_text=f'https://www.youtube.com/watch?v={link["id"]}'
        )
    ) for link in links]

    await query.answer(articles, cache_time=1, is_personal=True)






executor.start_polling(dp, skip_updates=True)



# import requests
# from bs4 import BeautifulSoup
# import re
#
#
# def searcher():
#     response = requests.get('https://www.youtube.com/results?search_query=python')
#     soup = BeautifulSoup(response.content, 'html.parser')
#     search = soup.find('script', string=re.compile('"videoId"'))
#     key = '"videoId":"'
#     data = re.findall(key+r"([^*]{11})", str(search))
#     print(data)
#
# searcher()