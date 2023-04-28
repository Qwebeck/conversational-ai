import discord
import os
from dotenv import load_dotenv
import MessageHandler as message_handler

TOKEN_KEY = 'TOKEN'


def run_discord_bot():
    TOKEN = os.getenv(TOKEN_KEY)
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(str(client.user) + " is currently running!")

    @client.event
    async def on_message(message):
        await message_handler.handle_message(message, client)

    client.run(TOKEN)


if __name__ == '__main__':
    load_dotenv()
    run_discord_bot()
