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

##  <img src="https://theme.zdassets.com/theme_assets/678183/84b82d07b293907113d9d4dafd29bfa170bbf9b6.ico" width="24"> Discord Bot 

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
# 6. Installation method
# 7. How to reproduce - step by step
## Infrastructure as Code approach
# 8. Demo deployment steps:
## Configuration set-up
## Data preparation
## Execution procedure
## Results presentation
# 9. Summary – conclusions
# Reference




