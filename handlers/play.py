from os import path

from pyrogram import Client
from pyrogram.types import Message, Voice

from callsmusic import callsmusic, queues
import wget
from os import path
import requests
import aiohttp
import youtube_dl
from youtube_search import YoutubeSearch


import converter
from downloaders import youtube

from config import BOT_NAME as bn, DURATION_LIMIT
from helpers.filters import command, other_filters
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import os
import aiohttp
import aiofiles
import ffmpeg
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def transcode(filename):
    ffmpeg.input(filename).output("input.raw", format='s16le', acodec='pcm_s16le', ac=2, ar='48k').overwrite_output().run() 
    os.remove(filename)

# Convert seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


# Change image size
def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

async def generate_cover(requested_by, title, views, duration, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    image1 = Image.open("./background.png")
    image2 = Image.open("etc/tg_vc_bot.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("temp.png")
    img = Image.open("temp.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("etc/font.otf", 32)
    draw.text((190, 550), f"Title: {title}", (255, 255, 255), font=font)
    draw.text(
        (190, 590), f"Duration: {duration}", (255, 255, 255), font=font
    )
    draw.text((190, 630), f"Views: {views}", (255, 255, 255), font=font)
    draw.text((190, 670),
        f"Added By: {requested_by}",
        (255, 255, 255),
        font=font,
    )
    img.save("final.png")
    os.remove("temp.png")
    os.remove("background.png")




@Client.on_message(command("play") & other_filters)
@errors
async def play(_, message: Message):

    lel = await message.reply("🔄 **Processing** sounds...")
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name

    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Support Group", url="https://t.me/Cutiepii_Support")
                   
                ]
            ]
        )

    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"❌ Videos longer than {DURATION_LIMIT} minute(s) aren't allowed to play!"
            )

        file_name = get_file_name(audio)
        title = file_name
        thumb_name = "https://telegra.ph/file/5a0e93a4503dbfad8a113.jpg"
        thumbnail = thumb_name
        duration = round(audio.duration / 60)
        views = "Locally added"
        keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
"💬 Support Group", url="https://t.me/Cutiepii_Support")

                    ]
                ]
            )
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)  
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )
    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
           # url = f"https://youtube.com{results[0]['url_suffix']}"
            #print(results)
            title = results[0]["title"][:40]       
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f'thumb{title}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            keyboard = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Watch On YouTube",
                                url=f"{url}")

                        ]
                    ]
                )
        except Exception as e:
            title = "NaN"
            thumb_name = "https://telegra.ph/file/5a0e93a4503dbfad8a113.jpg"
            duration = "NaN"
            views = "NaN"
            keyboard = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Watch On YouTube",
                                url=f"https://youtube.com")

                        ]
                    ]
                )
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)     
        file_path = await converter.convert(youtube.download(url))
    else:
        await lel.edit("🔎 **Finding** the song...")
        sender_id = message.from_user.id
        user_id = message.from_user.id
        sender_name = message.from_user.first_name
        user_name = message.from_user.first_name
        rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

        query = ''
        for i in message.command[1:]:
            query += ' ' + str(i)
        print(query)
        await lel.edit("🎵 **Processing** sounds...")
        ydl_opts = {"format": "bestaudio[ext=m4a]"}
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            #print(results)
            title = results[0]["title"][:40]       
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f'thumb{title}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]

        except Exception as e:
            lel.edit(
                "❌ Song not found.\n\nTry another song or maybe spell it properly."
            )
            print(str(e))
            return

        keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Watch On YouTube",
                            url=f"{url}")

                    ]
                ]
            )
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)  
        file_path = await converter.convert(youtube.download(url))
  
    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await message.reply_photo(
        photo="final.png", 
        caption=f"#⃣ Your requested song **queued** at position {position}!",
        reply_markup=keyboard)
        os.remove("final.png")
        return await lel.delete()
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        await message.reply_photo(
        photo="final.png",
        reply_markup=keyboard,
        caption=f"🏷 **Name:** [{title[:35]}]({url})\n⏳ **Duration:** {duration}\n" \
               + f"🎧 **Requested By:** {requested_by}\n📡 **Platform:** Deezer".format(
        message.from_user.mention()
        ),
    )
        os.remove("final.png")
        return await lel.delete()


# JioSaavn Play

@Client.on_message(
    filters.command("saavn")
    & filters.group
    & filters.edited
)
async def jiosaavn(client: Client, message_: Message):
    requested_by = message_.from_user.first_name
    chat_id=message_.chat.id
    text = message_.text.split(" ", 1)
    query = text[1]
    res = await message_.reply_text("🔄 **Processing** Sounds...")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://jevcplayerbot-saavndl.herokuapp.com/result/?query={query}"
            ) as resp:
                r = json.loads(await resp.text())
        sname = r[0]["song"]
        slink = r[0]["media_url"]
        ssingers = r[0]["singers"]
        sthumb = r[0]["image"]
        sduration = int(r[0]["duration"])
    except Exception as e:
        await res.edit(
            "Found Literally Nothing, You Should Work On Your English."
        )
        print(str(e))
        is_playing = False
        return
    file_path = await convert(wget.download(slink))
    await res.edit_text("🎵 Processing Sounds...")
    if message_.chat.id in tgcalls.pytgcalls.active_calls:
        position = sira.add(message_.chat.id, file_path)
        await client.send_photo(
        chat_id=message_.chat.id,
        photo="https://telegra.ph/file/5a0e93a4503dbfad8a113.jpg",
        caption=f"#️⃣ Your requested song queued at position {position}.",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Support Group", url="https://t.me/Cutiepii_Support")]]
        ),
        parse_mode="markdown") 
        await res.delete()
    else:
        tgcalls.pytgcalls.join_group_call(message_.chat.id, file_path)
        await client.send_photo(
        chat_id=message_.chat.id,
        caption=f"▶️ Playing `{sname}` Via [JioSaavn](https://t.me/Cutiepii_Support)",
        photo="https://telegra.ph/file/5a0e93a4503dbfad8a113.jpg",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Support Group", url="https://t.me/Cutiepii_Support")]]
        ),
        parse_mode="markdown")
        await res.delete()
