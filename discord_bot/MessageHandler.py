import discord
from azure.ai.textanalytics import TextAnalyticsClient
import WikipediaHttpClient as wiki_client
import WikiResponse as search_response
from collections import Counter
from itertools import chain


ERROR_INFO = "Cannot call Wikipedia API: "


async def handle_message(message: discord.Message, client: discord.Client, azure_client: TextAnalyticsClient):
    if message.author == client.user:
        return
    response = await prepare_answer(message, azure_client)
    if response:
        await send_message(message, response)


async def prepare_answer(message: discord.Message, azure_client: TextAnalyticsClient):
    cmd_name = message.content.split(' ')[0].removeprefix('/')
    handle = next(cmd for cmd in commands if cmd.__name__ == cmd_name)
    return await handle(message, azure_client)


async def search(message: discord.Message, *_):
    query = message.content.removeprefix('/search').strip()
    wiki_response = wiki_client.search(query)
    if wiki_response:
        return str(wiki_response)
    return ERROR_INFO + str(wiki_response)


async def help(*_):
    return """
    /help - display this message
    /search <query> - search Wikipedia for given query
    /recommend - recommend article based on recent searches
    """


async def recommend(message: discord.Message, azure_client: TextAnalyticsClient):
    await send_message(message, "Searching for recommendations...")
    search_responses = [
        search_response.WikiSearchResponse.from_search_response(msg.content) async for msg in message.channel.history(limit=10)
        if msg.content.startswith(search_response.FIRST_LINE)
    ]
    article_titles = chain(*[response.titles for response in search_responses])
    summaries = [wiki_client.get_summary(t) for t in article_titles]
    key_phrases = Counter(extract_key_phrases(azure_client, summaries))
    most_common = key_phrases.most_common(1)[0]
    return search_response.WikiRecomendationResponse(most_common[0], most_common[1], wiki_client.search(most_common[0]))


def extract_key_phrases(azure_client, summaries):
    keyphrases = []
    azure_documents_limit = 10
    for i in range(0, len(summaries), azure_documents_limit):
        keyphrases.extend(azure_client.extract_key_phrases(
            summaries[i:i+azure_documents_limit]))
    return [phrase for summary_extraction in keyphrases for phrase in summary_extraction.key_phrases]


async def send_message(user_message, response):
    try:
        await user_message.channel.send(str(response))
    except Exception as e:
        print(e)


commands = [search, help, recommend]
