#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = "28619451" config("API_ID", default=None, cast=int)
API_HASH = "e41e306cd0e0d0be11ec78c281f0b628" config("API_HASH", default=None)
BOT_TOKEN = "7072495432:AAHMFM3ejs_BZ0joIBq1_R0KOO1y3YNhFK8" config("BOT_TOKEN", default=None)
SESSION = "BAGobe0AjWCWbnYPtQGB_8EGMSpkC10XMy-RN4uM0bGPNuU6CjTNbhbeIeKnUVZUdnwPJnI2W_W50Q2Bh0qYHACxh3F0dA2Awsjnu03cNzZZoS27kZ8Y-smM3Tt1Hx95ll0zGyrLB36ziigKOkVNrdYQM_SWNsITgLpPRWV0UnOvj_R5EdOKFByzywhfKThjJB3-i39SYY9rRTEqzMwfFCFTRojARQ13KC8SmZ14dpSpLA17bytX8lwoawmG6eVD_ukfmk76w45b6O3jbqnm7LdFC56v_77FOqU03_mVdp5dSq0HMttjX7_K4whCEbVbPDJblMm_GdM9cRyk7GBdkUBobwEQCQAAAAE7BEmYAA" config("SESSION", default=None)
FORCESUB = "SmexyStore" config("FORCESUB", default=None)
AUTH = "5285104024" config("AUTH", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
