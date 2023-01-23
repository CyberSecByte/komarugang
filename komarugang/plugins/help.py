from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command(["help"]))
async def help(_, message):
    helptext= "This is a sample help message"
    await message.reply(helptext)