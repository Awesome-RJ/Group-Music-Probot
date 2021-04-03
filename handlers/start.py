from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>

I am Group Music Probot, I Am an Advance And Powerful Telegram Groups Voice Chat Music Bot.

To add in your group contact us at @Cutiepii_Support

/help Use the Commands Button For Commends List.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Management Bot", url="https://t.me/Cutiepii_Robot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Support Group", url="https://t.me/Cutiepii_Support"
                    ),
                    InlineKeyboardButton(
                        "Updates Channel", url="https://t.me/Techno_Ocean"
                    ),
                    InlineKeyboardButton(
                        "Music Lovers", url="https://t.me/Hindi_K_Drama_1" )
                ],
                [
                    InlineKeyboardButton(
                        "Developer", url="https://t.me/Awesome_RJ"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
    
    
@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
f"""<b> Hy Music Lover {message.from_user.first_name} Commends Are Here</b>

/reload -> To search the song on Youtube and play the first matching result.
/saavn -> To search song on jio saavan and play the first result
/deezer -> To search song on deezer and play good quality stream.
/play -> Reply this in response to a link or any telegram audio file it will be played.
/pause -> to pause the stream.
/skip -> to skip current song
/resume -> to resume the playback.
/stop or /kill -> to stop the streaming of song.

Note:- Add Assistant And Bot Make Admin Then Promote To Admin.
""",
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Assistant", url="https://t.me/Group_music_pro"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Support Group", url="https://t.me/Cutiepii_Support"
                    ),
                    InlineKeyboardButton(
                        "Updates Channel", url="https://t.me/Techno_Ocean"
                    ),
                    InlineKeyboardButton(
                        "Music Lovers", url="https://t.me/Hindi_K_Drama_1" )
                ],
                [
                    InlineKeyboardButton(
                        "Group Management Bot", url="https://t.me/Cutiepii_Robot"
                    )
                ]
            ]
        )
    )

