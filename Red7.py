
from .. import pbot as Red7 
from pyrogram import filters
from pyrogram.types import ChatMemberUpdated
try:
   from RiZoeLX.functions import Red7_Watch
except:
   import os
   os.system("pip3 install pyRiZoeLX==1.1.3")
   from RiZoeLX.functions import Red7_Watch

@Red7.on_chat_member_updated(filters.group, group=69)
async def Red7Scanner(_, member: ChatMemberUpdated):
   await Red7_Watch(Red7, member)