import WikipediaHttpClient as wiki_client

SEARCH = "/search"
HELP = "/help"

HELP_MESSAGE = " # SAMPLE HELP MESSAGE #"
ERROR_INFO = "Cannot call Wikipedia API: "


async def handle_message(message, client):
    if message.author == client.user:
        return
    else:
        response = prepare_answer(message.content)
        if response:
            await send_message(message, response)


def prepare_answer(message_content):
    if message_content.startswith(SEARCH):
        query = message_content.removeprefix(SEARCH)
        wiki_response = wiki_client.make_wikipedia_request(query)
        if wiki_response:
            return str(wiki_response)
        else:
            return ERROR_INFO + str(wiki_response)
    elif message_content.startswith(HELP):
        return HELP_MESSAGE


async def send_message(user_message, response):
    try:
        await user_message.channel.send(response)
    except Exception as e:
        print(e)
