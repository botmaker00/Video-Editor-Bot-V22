import os

API_ID = int(os.getenv("API_ID", 21518327))
API_HASH = os.getenv("API_HASH", "e72f588b3e4763f01eecfc3c4aa7e8ac")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8147773795:AAEy3BTQv042lrFqcQJzSAPi81fx3_A4UyU")
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://userbot:userbot@cluster0.iweqz.mongodb.net/test?retryWrites=true&w=majority")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", -1001839965169))
