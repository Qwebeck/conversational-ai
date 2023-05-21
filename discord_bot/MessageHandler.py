import discord
from azure.ai.textanalytics import TextAnalyticsClient
import WikipediaHttpClient as wiki_client
import WikiResponse as search_response
from collections import Counter

HELP_MESSAGE = """"""

ERROR_INFO = "Cannot call Wikipedia API: "


async def handle_message(message: discord.Message, client: discord.Client, azure_client: TextAnalyticsClient):
    if message.author == client.user:
        return
    response = await prepare_answer(message, azure_client)
    if response:
        await send_message(message, response)


async def search(message: discord.Message, *_):
    query = message.content.removeprefix('/search').strip()
    wiki_response = wiki_client.search(query)
    if wiki_response:
        return str(wiki_response)
    return ERROR_INFO + str(wiki_response)


async def help(*_):
    return HELP_MESSAGE


async def recommend(message: discord.Message, azure_client: TextAnalyticsClient):
    search_responses = [
        msg.content async for msg in message.channel.history(limit=50)
        if msg.content.startswith(search_response.FIRST_LINE)
    ]
    article_titles = [l.split('/')[-1]
                      for r in search_responses
                      for l in r.split('\n')[1:]
                      ]
    summaries = [wiki_client.get_summary(t) for t in article_titles]
    key_phrases = Counter([str(phrase.key_phrases)
                          for phrase in azure_client.extract_key_phrases(summaries)])
    most_common = key_phrases.most_common(1)
    return wiki_client.search(most_common)


async def send_message(user_message, response):
    try:
        await user_message.channel.send(response[:4000])
    except Exception as e:
        print(e)


commands = [search, help, recommend]
command_names = [f'/{cmd.__name__}' for cmd in commands]


async def prepare_answer(message: discord.Message, azure_client: TextAnalyticsClient):
    cmd_name = message.content.split(' ')[0].removeprefix('/')
    handle = next(cmd for cmd in commands if cmd.__name__ == cmd_name)
    return await handle(message, azure_client)
