import os
class Config(object):
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    API_HASH  = os.getenv("API_HASH")
    API_ID    = os.getenv("API_ID")
    SUDO_USERS_ID = os.getenv("SUDO_USERS_ID")
    WELCOME_DELAY_KICK_SEC = os.getenv("WELCOME_DELAY_KICK_SEC")
    OWNER_USER_ID = os.getenv("OWNER_USER_ID")

JSMAPI= "https://jiosaavnapi.bhadoo.uk/result/?query=" 
