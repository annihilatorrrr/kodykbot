# KodyK Bot 

[![Python](http://forthebadge.com/images/badges/made-with-python.svg)](https://python.org)

Just Another Telegram Bot Written In Python Using Pyrogram.

### Features
```
Hello NoobCoder, these are some commands you can try with the BOT,
        
        General:
        /areuded To Check if the bot is Alive
        /creator Creator's GitHub Profile
        /sourcecode Link to GitHub Repo
        /website Creator's Website
        /wikipedia Search For Articles in Wikipedia
        /quote Get Quotes
        /crackjoke Get A Geeky Joke
        /stackoverflow Search For Answers in StackOverFlow
        /dlmusic Download Music from YouTube and SoundCloud  
        /saavndl Download Music from JioSaavn
        /howzdweather Get Weather Report of a City
        
        Owner:
        /l To run your Python Code from Telegram 
        /shutdown Shutdown the Linux Machine on which the bot is running
        /cancelshutdown Cancel Shutdown

        Group Management:
        /mutenow Mute a User
        /unmutenow Unmute a User
        /delete Delete a Message
      

        Will add more commands soon...

```

### Requirements

- Python 3.6 or higher.
- A [Telegram API key](//docs.pyrogram.org/intro/setup#api-keys).
- A [Telegram bot token](//t.me/botfather).

### Deploy on Heroku
[<img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku" height="40"/>](https://heroku.com/deploy?template=https://github.com/Kody-K/kodykbot "Heroku")

## OR

### Manual Installation

```
$ git clone https://github.com/Kody-K/kodykbot
$ cd kodykbot
$ pip3 install -r requirements.txt
```

Replace these lines in `config.py`: 

```
import os
class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    API_HASH  = os.getenv("API_HASH")
    API_ID    = os.getenv("API_ID")
    SUDO_USERS_ID = os.getenv("SUDO_USERS_ID")
    WELCOME_DELAY_KICK_SEC = os.getenv("WELCOME_DELAY_KICK_SEC")
    OWNER_USER_ID = os.getenv("OWNER_USER_ID")
```

with this:

```
BOT_TOKEN = str("bot token here")
API_HASH  = str("api hash here") 
API_ID    = int(api_id_here)
SUDO_USERS_ID = str("sudo users id here")
WELCOME_DELAY_KICK_SEC = 300
OWNER_USER_ID = int(your_user_id_here)
```

#### Usage 

```
$ python3 bot.py
```

Wait until you see this...

```
Pyrogram v1.1.13, Copyright (C) 2017-2021 Dan <https://github.com/delivrance>
Licensed under the terms of the GNU Lesser General Public License v3 or later (LGPLv3+)
```

Your Bot Has Successfully started now...











