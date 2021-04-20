from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

GROUP_MUSIC_PROBOT_IMG= "https://telegra.ph/file/70008107133ae8f4d1f1f.jpg"

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
      await message.reply_text("""**💜 Group Music Probot is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎙️ Support Group 🎙️", url="https://t.me/Cutiepii_Support")
                ]
            ]
        )
   )

