import logging
from Group_Music_Probot.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from Group_Music_Probot.config import ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME

from Group_Music_Probot.config import BOT_NAME as bn


GROUP_MUSIC_PROBOT_IMG = "https://telegra.ph/file/70008107133ae8f4d1f1f.jpg"

logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_photo(GROUP_MUSIC_PROBOT_IMG)
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵
I am Group Music Probot, I Am an Advance And Powerful Telegram Groups Voice Chat Music Bot.
Note:- Add @Group_music_pro and @Group_music_Probot to your group and make an admin.
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Commands 🛠", url="https://telegra.ph/Commands-04-20")
                  ],[
                    InlineKeyboardButton(
                        "💬 Music Lovers", url="https://t.me/Hindi_K_drama_1"
                    ),
                    InlineKeyboardButton(
                        "💬 Support Group", url="https://t.me/Cutiepii_Support"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "💁 Assistant 💁", url="https://t.me/Group_Music_Pro"
                    )],
                    [ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/Group_Music_ProBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

    

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        f"""*💜 {PROJECT_NAME} is online**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Support Chat", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '▶️', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [InlineKeyboardButton("➕ Add me to your Group 🙋‍♀️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton(text = '📲 Updates', url=f"https://t.me/{UPDATES_CHANNEL}"),
             InlineKeyboardButton(text = '💬 Support', url=f"https://t.me/{SUPPORT_GROUP}")],
            [InlineKeyboardButton(text = '🌐 Network', url=f"https://t.me/Yuki_Network")],
            [InlineKeyboardButton(text = '◀️', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '◀️', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '▶️', callback_data = f"help+{pos+1}")
            ],
        ]
    return button

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**🙋‍♀️ Hello there! I can play music in the voice chats of telegram groups & channels.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🟣 Click here for help 🟣", url=f"https://t.me/{BOT_USERNAME}?start"
                    )
                ]
            ]
        ),
    )

