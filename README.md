# code-status-bot

======

## Overview

For these people who work with programs, simulations, training, and different computational process that takes a large amount of time. code-status-bot is a discord bot to keep an online tracking of the status of your code. This bot takes the information from a JSON file and sends it to you thanks to a discord server.

The goal of code-status-bot is to keep yourself informed of the advance of your running program while you are away from your computer.

## Installation & running

## Requerimients

* [Python](https://www.python.org/)
* [discord.py](https://pypi.org/project/discord.py/)

The installation really is effortless. The code should work with the most updated versions of requeriments, how ever here are the versions that i use to run the bot.

* Python 3.7.9
* discord.py 1.5.1

## How to use

## Add the bot to a discord server

First of all you need to have a discord server where you want to deploy the bot. I recomend follow the [tutorial](https://discordpy.readthedocs.io/en/latest/discord.html) given by the oficial documentation. Save the token generated in the setup process

### JSON file

The program thath you want to track should write a JSON file with the next structure

```json
{
    "vars": {
        "Name of main var to show in activiry of the bot": value,
        "var2": value,
        ...,
        "varn": value
    },
    "errors": [
        "Error1",
        ...,
        "Errorn"
    ],
    "var_activity_bot": "Name of main var to show in activiry of the bot"
}
```

NOTE that "var_activity_bot" is a reservated key in the dictionary where you have to put the name of the most important variable thath you want to keep an eye on. This variable will show in the activity field of the bot status.

the full path to your JSON file have to be in the definition of the flag "bot.FILE_PATH" in the bot_main.py file

```Python
bot.FILE_PATH = full path to your JSON file
```

You may desire to read this file in a specific frecuency, it all depence of the complexity of your program, therefore you have to setup this fixed time.

the full path to your JSON file have to be in the definition of the flag "bot.FILE_PATH" in the bot_main.py file

```Python
bot.MINUTES_TO_WAIT_LOOP = some float time in minutes
```

### Run the code

```python
python bot_main.py
```
