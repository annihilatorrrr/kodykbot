HEROKU = False

if HEROKU:
	import os
	BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
	API_ID = int(os.environ.get("API_ID", 6))
	API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
	SUDO_USERS_ID = list(int(x) for x in os.environ.get("SUDO_USERS_ID", "").split())
	WELCOME_DELAY_KICK_SEC = int(os.environ.get("WELCOME_DELAY_KICK_SEC", None))
	OWNER_USER_ID = int(os.environ.get("OWNER_USER_ID", None))
	JSMAPI= os.environ.get("JSMAPI", None)


if not HEROKU:
	BOT_TOKEN = "6464634:ASbfhSHjf-LMSBadsf963szFAF"
	API_ID = 541534
	API_HASH = "ds5g4sd1gd45gds"
	SUDO_USERS_ID = [123444613, 547453154] # Sudo users have full access to everythin, don't trust anyone
	OWNER_USER_ID = 8563321512
	WELCOME_DELAY_KICK_SEC = 300
	JSMAPI = "https://jiosaavnapi.bhadoo.uk/result/?query="
