import discord
import os
from dotenv import load_dotenv
import MessageHandler as message_handler
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from discord.ext import commands

TOKEN_KEY = 'TOKEN'


def run_discord_bot():
    token = os.getenv(TOKEN_KEY)
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    azure_client = initialize_azure_client()

    @client.event
    async def on_ready():
        print(str(client.user) + " is currently running!")

    @client.event
    async def on_message(message: discord.Message):
        await message_handler.handle_message(message, client, azure_client)

    assert token
    client.run(token)


def initialize_azure_client():
    # Create client using endpoint and key
    cog_endpoint = os.getenv('COG_SERVICE_ENDPOINT')
    cog_key = os.getenv('COG_SERVICE_KEY')
    assert cog_endpoint and cog_key
    credential = AzureKeyCredential(cog_key)
    client = TextAnalyticsClient(endpoint=cog_endpoint, credential=credential)
    return client


if __name__ == '__main__':
    load_dotenv()
    run_discord_bot()
