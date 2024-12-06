import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "13892075"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "e3b8632e5034801fbeaea7aa3283f442")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://toxichackz:Arjun10080@cluster0.ffa4h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
