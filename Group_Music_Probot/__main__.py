


import requests
from pyrogram import Client as Bot

from Group_Music_Probot.config import API_HASH
from Group_Music_Probot.config import API_ID
from Group_Music_Probot.config import BG_IMAGE
from Group_Music_Probot.config import BOT_TOKEN
from Group_Music_Probot.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Group_Music_Probot.modules"),
)

bot.start()
run()
