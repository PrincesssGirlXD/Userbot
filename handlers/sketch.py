from pyrogram import Client 
from pyrogram import filters
from pyrogram.types import Message
from handlers.help import *
from PIL import Image


@Client.on_message(filters.command("sketch", ["-"]) & filters.me)
async def example(client: Client, message: Message):
    x = await message.edit("<Strong>Making Sketch...</Sketch>")
    image_file = Client.download_media("image.jpg")
    image = Image.open(image_file)
    image = image.convert("L")
    image = Image.eval(image, lambda x: 255-x)
    image.save("sketch.jpg")
    Client.send_photo("sketch.jpg")
    await x.edit("<Strong>Sketch Successfully Printed</Strong>")
