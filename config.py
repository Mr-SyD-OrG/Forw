# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper



import os

class Config:
    API_ID = os.environ.get("API_ID", "")
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    BT_TOKEN = os.environ.get("BT_TOKEN", "") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "forward-bot") 
    BT_SESSION = os.environ.get("BT_SESSION", "mrsyd-bot") 
    DB_URL = os.environ.get("DB_URL", "")
    PORT = os.environ.get("PORT", "8080")
    DB_NAME = os.environ.get("DB_NAME", "cluster0")
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '').split()]


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    






# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
