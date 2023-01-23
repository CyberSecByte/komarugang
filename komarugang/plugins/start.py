from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command(["start"]))
async def start(_, message):
    text= "Meow Meow"
    await message.reply_photo(
        caption=text,
        photo="https://raw.githubusercontent.com/CyberSecByte/imgdumps/master/komaru.jpg")
