from os import environ 

class Config:
    API_ID = environ.get("API_ID", "27815405")
    API_HASH = environ.get("API_HASH", "4e70821cd2af3322f7cf2f2887e32821")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6360827839:AAFb5YQwkZSdJ9cWwuAjNisTkowsu2szcks") 
    BOT_SESSION = environ.get("BOT_SESSION", "BQGobe0ACJXMmBnzFGXaE9eEglH7p6RRtrTsASejIW7pkRHbj-lfEWcENQ0mjdkaOxxeILd53VNfgjUepSZ4rQtCWGigbL3VJOXu7ZIcxDJLSDkOrRsHF_VY32o4n2SoKbbtQ4_BJMUKWqUUpzw17eDg5tSDGvVbuM_ofRkbEMg_zbAaVsiTgWJnYdtYMwgVUn4qweTLtFgy5SSt3ATwN1YG3nyANRyn7mCE_pyzKIBvZNMnjS61Qdm8tOysa47RWr2RWFiZXzmQXyDB9RPTHMCBamYidRmoOVyCQn1-EzQpGnmUnEeWdqqsjJxXkMNp61FEClwz-1ZkzHXugO3WDiDmjYrx8gAAAAGOJFsyAA") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://t14012318:pJoLHqidazIlyVKj@cluster0.p4uurti.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6679714610').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
