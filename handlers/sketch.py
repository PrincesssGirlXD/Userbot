from pyrogram import Client 
from pyrogram import filters
from pyrogram.types import Message
from handlers.help import *
from PIL import Image



@Client.on_message(filters.command("sketch", ["-"]) & filters.me)
async def progress(client: Client, message: Message):
    x = await message.edit("<Strong>Making Sketch...</Sketch>")
    user = message.from_user.id
    image = await Image.open(user)
    image = await image.convert("L")
    image = await Image.eval(image, lambda x: 255-x)
    await image.save("sketch.jpg")
    await Client.send_photo("sketch.jpg")
    await x.edit("<Strong>Sketch Successfully Printed</Strong>")
