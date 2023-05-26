Acronym - Title: CONVAI-12
Authors: Bohdan Forostianyi, Jakub Koźliak
Year, Group: 2023, group 4

Contents list

# 1. Introduction

The bot is designed to act as an intermediary between Discord users and the Wikipedia platform. It will leverage the [Wikipedia API](https://en.wikipedia.org/w/api.php?action=help&modules=query) to provide users with access to relevant information and resources from the platform directly through Discord.

Additionally, the bot will include a feature that allows users to receive recommendations for similar articles based on their search history or by passing an article as an argument. This feature will provide users with a personalized experience and facilitate discovery of related topics of interest.

# 2. Theoretical background/technology stack

Application will consists of two parts: first is a bot itself, second - language extraction model based in the cloud which will be able to analyze user history and provide recomendations.

## Language Model

As a model provider will be used Microsoft Azure and its [KeyPhrases Service](https://learn.microsoft.com/en-us/connectors/cognitiveservicestextanalytics/?context=%2Fazure%2Fcognitive-services%2Flanguage-service%2Fcontext%2Fcontext&fbclid=IwAR3jIeFY1hPbyTBLq55i17pqwRCWCPj4OO-mncsk-T7_4oPZ_WBOLEJQaBk#async-keyphrases-(2022-05-01))

Normally this service is paid

![image](https://user-images.githubusercontent.com/21079319/228912379-64e183f8-43bc-46ba-a30d-53a5b5334614.png)

however, Azure allows for creation of a free account which goes with `200 USD` credits for use in the first month, which should be sufficient for demo.

![image](https://user-images.githubusercontent.com/21079319/228914251-d13bb603-6a61-4e3a-989f-ea721ccc6184.png)

## <img src="https://theme.zdassets.com/theme_assets/678183/84b82d07b293907113d9d4dafd29bfa170bbf9b6.ico" width="24"> Discord Bot

Bot part of the project will be based on Python [Discord API](https://discord.com/developers/docs/intro)

It allows to extend basic Discord Server functionality by making event driven application for custom handling user's behaviour,
in our case: reacting for text chat messages defined below.

Discord API provides easy way to integrate with user's Server by attaching extension to Server configuration.

# 3. Case study concept description

The bot with provide users with two commands:

- `/search [query]` - which will search for an articles with title matching provided `query` and disaply it on Discord
- `/recommend` - which will recommend articles to the user based on his search history

# 4. Solution architecture

## Architecture Diagram

![Blank diagram - Page 1](https://user-images.githubusercontent.com/80708447/233092309-cc6e9dd9-95c2-474e-a23f-38cc9ea3b9a8.png)

## Sequential diagram of proposed queries

![Blank diagram - Sequence diagram](https://user-images.githubusercontent.com/80708447/233092448-af865d80-6597-4589-8c2c-c38e578fecd9.png)

# 5. Environment configuration description

Our bot will be used on Discord Server as an extension for regular text channels. By default it will be available for every user on server, allowing them to search articles using WikipediaAPI.

Bot will need access to KeyPhraseService, which can be configured during bot installation on Discord Server.

WikipediaAPI is free to use, no need for further configuration.

# 6. Installation method

In order to install and bot install dependencies from `requirements.txt` file with `pip install -r requirements.txt`.

# 7. How to reproduce - step by step

(assuming that you want to add bot to your existing server)

1. Clone repository, install dependencies and configure `.env` file (see [Configuration set-up](#configuration-set-up))
2. To start a bot you should run `python bot.py` command.
3. Add bot to your server, you can use this link: <https://discord.com/api/oauth2/authorize?client_id=[CLIENT_ID]&permissions=0&scope=bot>, where your should replace `[CLIENT_ID]` with your bot's client id (you can get it from Discord Developer Portal -> Applications -> [Your Application] -> OAuth2 -> Client ID)

# 8. Demo deployment steps

## Configuration set-up

Create `.env` file with following variables:
    - `DISCORD_TOKEN` - token for Discord Bot (you can get it from Discord Developer Portal -> Applications -> [Your Application] -> Bot -> Token)
    - `KEY_PHRASE_SERVICE_ENDPOINT` - endpoint for KeyPhraseService (you can get it from Azure Portal -> Resources -> [Your Resource Name] -> Keys and Endpoints -> Endpoint)
    - `KEY_PHRASE_SERVICE_KEY` - key for KeyPhraseService (you can get it from Azure Portal -> Resources -> [Your Resource Name] -> Keys and Endpoints -> Key 1)

## Execution procedure

On your server type: `/search [query]` to search for an article with title matching provided `query`.
Bot will return 10 articles most relevant to your request.
After that run recommend, which will return 10 articles most relevant to your search history.

## Results presentation
Let's assume our user was recently interested in fantasy and searched for topics related to orcs and to world of Warcraft, as it shown below.

![image](https://github.com/Qwebeck/conversational-ai/assets/21079319/84b5f224-4b93-49d3-97b5-e776bb874d4b)
 
![image](https://github.com/Qwebeck/conversational-ai/assets/21079319/e6114ccd-50c8-446d-83bb-dffce91850e3)


After some time he found an information about everything he needed and decides to ask for recomendation.
So he types command `recommend` and he is presented with the following results
![image](https://github.com/Qwebeck/conversational-ai/assets/21079319/6bffafa1-3345-4bc0-a2f5-42e41aacf6ef)



# 9. Summary – conclusions

Discord provides a simple way to extend its functionality by creating custom bots which does not require a lot of configuration. Messanger nature of Discord makes it a perfect platform for conversational AIs, that can interact with users and help them with their daily tasks, by reading text messages or even interacting with voice commands.
In this project we deomnstrated how to create a simple bot which can search Wikipedia articles and recommend new ones based on user's search history.
The platform used for Conversational AI was Microsoft Azure, which provides a lot of services for Natural Language Processing, including KeyPhraseService.
However, it is not the only one, and we do claim that it is the cheapest one: during development authors made requests to approximately 200 documents extractions and spent 20$ of their subscription.
So before using it in production more in depth comparison between other provides (e.g. Amazon, OpenAI) should be done before making a decision.

# Reference

* [Discord API](https://discord.com/developers/docs/intro)
- [Wikipedia API](https://en.wikipedia.org/w/api.php?action=help&modules=query)
- [Azure Language Services](https://learn.microsoft.com/en-us/connectors/cognitiveservicestextanalytics)
