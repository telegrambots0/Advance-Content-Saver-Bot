from os import environ 

class Config:
    API_ID = environ.get("API_ID", "28619451")
    API_HASH = environ.get("API_HASH", "e41e306cd0e0d0be11ec78c281f0b628")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7072495432:AAHMFM3ejs_BZ0joIBq1_R0KOO1y3YNhFK8") 
    BOT_SESSION = environ.get("BOT_SESSION", "BAGobe0AjWCWbnYPtQGB_8EGMSpkC10XMy-RN4uM0bGPNuU6CjTNbhbeIeKnUVZUdnwPJnI2W_W50Q2Bh0qYHACxh3F0dA2Awsjnu03cNzZZoS27kZ8Y-smM3Tt1Hx95ll0zGyrLB36ziigKOkVNrdYQM_SWNsITgLpPRWV0UnOvj_R5EdOKFByzywhfKThjJB3-i39SYY9rRTEqzMwfFCFTRojARQ13KC8SmZ14dpSpLA17bytX8lwoawmG6eVD_ukfmk76w45b6O3jbqnm7LdFC56v_77FOqU03_mVdp5dSq0HMttjX7_K4whCEbVbPDJblMm_GdM9cRyk7GBdkUBobwEQCQAAAAE7BEmYAA") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5285104024').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
