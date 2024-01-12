import json
from pyrogram import Client, filters
from pyrogram.enums import ChatMembersFilter
from pyrogram import enums
import json
from pyrogram import Client, filters
from AnonXMusic import app

casery = "mvhmed"
DEVS =[f"{casery}"]

@app.on_message(filters.command("رفع مطور", "") & filters.group, group=5458658)
async def mazojgvmbie(client, message):
  if not message.from_user.username in casery:
    return
  user_id = message.reply_to_message.from_user.id
  user = await client.get_chat_member(message.chat.id, user_id)
  DEVS.append(user.user.username)
  await message.reply_text(f"تم رفع {message.reply_to_message.from_user.mention} المطور بنجاح")
            
@app.on_message(filters.command("المطورين", "") & filters.group, group=54642893)
async def getbannbvnbedusers(client, message):
  if not message.from_user.username in casery:
    return
  caesar = "قائمة المطورين:\n\n"
  for username in DEVS:
      caesar += f"- @{username}\n" 
  await message.reply_text(caesar)
  
@app.on_message(filters.command("تنزيل مطور", "") & filters.group, group=546565)
async def unbanncbb_user(client, message):
  if not message.from_user.username in casery:
    return
  user_id = message.reply_to_message.from_user.id
  user_username = message.reply_to_message.from_user.username
  if user_username in DEVS:
    DEVS.remove(user_username)
    await message.reply_text("تم تنزيل المطور بنجاح")
  else:
    await message.reply_text("هذا المستخدم ليس مطورًا")
