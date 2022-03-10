import requests
from pyrogram import Client as Bot

from Group_Music_Probot.config import API_HASH, API_ID, BG_IMAGE, BOT_TOKEN
from Group_Music_Probot.services.callsmusic import run

response = requests.get(BG_IMAGE)
with open("./etc/foreground.png", "wb") as file:
    file.write(response.content)
bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Group_Music_Probot.modules"),
)

bot.start()
run()
