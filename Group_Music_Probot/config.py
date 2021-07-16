from os import getenv
import os
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Black_Knights_Union")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/f2659b2bb623d85053a4b.png")
admins = {}
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Group_Music_Pro")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Black_Knights_Union_Support")
PROJECT_NAME = getenv("PROJECT_NAME", "c")
SOURCE_CODE = getenv("SOURCE_CODE", "https://github.com/Awesome-RJ/Group-Music-Probot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))