from pyrogram import *
from config import Config
import asyncio
import random
from .Script import script
from .db import *
import re
from pyrogram.errors import FloodWait
from pyrogram.types import *
ADMIN = Config.OWNER_ID
SYD = "https://envs.sh/c77.jpg https://envs.sh/cKM.jpg https://envs.sh/c78.jpg https://envs.sh/c7U.jpg https://envs.sh/c7k.jpg https://envs.sh/c74.jpg https://envs.sh/c71.jpg https://envs.sh/c7R.jpg https://envs.sh/c7Y.jpg https://envs.sh/c73.jpg https://envs.sh/c7z.jpg https://envs.sh/c7K.jpg https://envs.sh/cKO.jpg https://envs.sh/cKm.jpg".split()
@Client.on_message(filters.command("start") & filters.private)
async def strtCap(bot, message):
    user_id = int(message.from_user.id)
    await insert(user_id)
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("⨭ Δᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇL ⨮", url=f"https://t.me/AutoCaption_Robot?startchannel=true")
            ],[
                InlineKeyboardButton("✭ Hᴇʟᴘ", callback_data="help"),
                InlineKeyboardButton("Aʙᴏᴜᴛ ✭", callback_data="about")
            ],[
                InlineKeyboardButton("⚝ Uᴘᴅᴀᴛᴇ", url=f"https://t.me/Bot_Cracker"),
                InlineKeyboardButton("Mᴏᴠɪᴇ ⚝", url=r"https://t.me/Mod_Moviez_X")
        ]]
    )
    await message.reply_photo(
        photo=random.choice(SYD),
        caption=f"<b>Hᴇʟʟᴏ {message.from_user.mention}\n\nɪ ᴀᴍ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ᴇᴅɪᴛ ʙᴏᴛ ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.\n\nFᴏʀ ᴍᴏʀᴇ ɪɴғᴏ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.\n\nMᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ » <a href='https://t.me/Bot_Cracker'>Bᴏᴛ Cʀᴀᴄᴋᴇʀ 🎋</a>\n\n<spoiler>Cʀᴇᴅɪᴛ ɢᴏᴇs ᴛᴏ:- <a href='https://t.me/Mod_Moviez_X'>Mᴏᴅ Mᴏᴠɪᴇᴢ X ✨</a></spoiler></b>",
        reply_markup=keyboard
    )

@Client.on_message(filters.private & filters.user(ADMIN)  & filters.command(["total_users"]))
async def all_db_users_here(client,message):
    silicon = await message.reply_text("Please Wait....")
    silicon_botz = await total_user()
    await silicon.edit(f"Tᴏᴛᴀʟ Usᴇʀ :- `{silicon_botz}`")

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
    if (message.reply_to_message):
        silicon = await message.reply_text("Geting All ids from database..\n Please wait")
        all_users = await getid()
        tot = await total_user()
        success = 0
        failed = 0
        deactivated = 0
        blocked = 0
        await silicon.edit(f"ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ...")
        async for user in all_users:
            try:
                time.sleep(1)
                await message.reply_to_message.copy(user['_id'])
                success += 1
            except errors.InputUserDeactivated:
                deactivated +=1
                await delete({"_id": user['_id']})
            except errors.UserIsBlocked:
                blocked +=1
                await delete({"_id": user['_id']})
            except Exception as e:
                failed += 1
                await delete({"_id": user['_id']})
                pass
            try:
                await silicon.edit(f"<u>ʙʀᴏᴀᴅᴄᴀsᴛ ᴘʀᴏᴄᴇssɪɴɢ</u>\n\n• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {tot}\n• sᴜᴄᴄᴇssғᴜʟ: {success}\n• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}\n• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}\n• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}")
            except FloodWait as e:
                await asyncio.sleep(t.x)
        await silicon.edit(f"<u>ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ</u>\n\n• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {tot}\n• sᴜᴄᴄᴇssғᴜʟ: {success}\n• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}\n• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}\n• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}")

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("restart"))
async def restart_bot(b, m):
    silicon = await b.send_message(text="**🔄 𝙿𝚁𝙾𝙲𝙴𝚂𝚂𝙴𝚂 𝚂𝚃𝙾𝙿𝙴𝙳. 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶...**", chat_id=m.chat.id)       
    await asyncio.sleep(3)
    await silicon.edit("**✅️ ʙᴏᴛ ɪꜱ ʀᴇꜱᴛᴀʀᴛᴇᴅ. 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝙼𝙴**")
    os.execl(sys.executable, sys.executable, *sys.argv)

@Client.on_message(filters.command("set_cap") & filters.channel)
async def setCap(bot, message):
    if len(message.command) < 2:
        return await message.reply(
            "Usᴀɢᴇ: **<code>/set_cap Yᴏᴜʀ Cᴀᴩᴛɪᴏɴ Hᴇʀᴇ</code> /n Sᴏᴍᴇ Vᴀʀɪᴀʙʟᴇꜱ Fᴏʀ Cᴀᴩᴛɪᴏɴ Aʀᴇ Sʜᴏᴡɴ Iɴ Tʜᴇ Hᴇʟᴩ Pᴀɢᴇ🫧 /n/n✓ Eᴠᴇʀʏᴛʜɪɴɢ Cʟᴇᴀʀ? Hᴏᴩɪɴɢ ✨ /n Exᴀᴍᴩʟᴇ: <code>/set_cap /n{file_name}/n/n⚙️ Size » {file_size}/n🌐 Lang » {language}/n🗓️ Year » {year}/n/n╔═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╗/n💥 𝙅𝙊𝙄𝙉 :- ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ /n💥 𝙅𝙊𝙄𝙉 :Hin|ʜᴀɴɴᴇʟ ʟɪɴᴋ/n╚═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╝</code>`**"
        )
    chnl_id = message.chat.id
    caption = (
        message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else None
    )
    chkData = await chnl_ids.find_one({"chnl_id": chnl_id})
    if chkData:
        await updateCap(chnl_id, caption)
        return await message.reply(f"Your New Caption: {caption}")
    else:
        await addCap(chnl_id, caption)
        return await message.reply(f"Yᴏᴜʀ Nᴇᴡ Cᴀᴘᴛɪᴏɴ Is: {caption}")

@Client.on_message(filters.command("del_cap") & filters.channel)
async def delCap(_, msg):
    chnl_id = msg.chat.id
    try:
        await chnl_ids.delete_one({"chnl_id": chnl_id})
        return await msg.reply("<b><i>✓ Sᴜᴄᴄᴇssғᴜʟʟʏ... Dᴇʟᴇᴛᴇᴅ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ Nᴏᴡ I ᴀᴍ Usɪɴɢ Mʏ Dᴇғᴀᴜʟᴛ Cᴀᴘᴛɪᴏɴ </i></b>")
    except Exception as e:
        e_val = await msg.replay(f"ERR I GOT: {e}")
        await asyncio.sleep(5)
        await e_val.delete()
        return

def extract_language(default_caption):
    language_pattern = r'\b(Hindi|English|Tamil|Telugu|Malayalam|Mal|Tam|Tel|Eng|Kan|Urd|Urdu|Japanese|Jap|Chinese|Bengali||Arabic|Kannada|Hin)\b'#Contribute More Language If You Have
    languages = set(re.findall(language_pattern, default_caption, re.IGNORECASE))
    if not languages:
        return "[Audio]"
    return ", ".join(sorted(languages, key=str.lower))

def extract_year(default_caption):
    match = re.search(r'\b(19\d{2}|20\d{2})\b', default_caption)
    return match.group(1) if match else None

@Client.on_message(filters.channel)
async def reCap(bot, message):
    chnl_id = message.chat.id
    default_caption = message.caption
    if message.media:
        for file_type in ("video", "audio", "document", "voice"):
            obj = getattr(message, file_type, None)
            if obj and hasattr(obj, "file_name"):
                file_name = obj.file_name
                file_size = obj.file_size
                language = extract_language(default_caption)
                year = extract_year(default_caption)
                file_name = (
                    re.sub(r"@\w+\s*", "", file_name)
                    .replace("_", " ")
                    .replace(".", " ")
                )
                cap_dets = await chnl_ids.find_one({"chnl_id": chnl_id})
                try:
                    if cap_dets:
                        cap = cap_dets["caption"]
                        replaced_caption = cap.format(file_name=file_name, file_size=get_size(file_size), default_caption=default_caption, language=language, year=year)
                        await message.edit(replaced_caption)
                    else:
                        replaced_caption = DEF_CAP.format(file_name=file_name, file_size=get_size(file_size), default_caption=default_caption, language=language, year=year)
                        await message.edit(replaced_caption)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    continue
    return

# Size conversion function
def get_size(size):
    units = ["Bytes", "Kʙ", "Mʙ", "Gʙ", "Tʙ", "Pʙ", "Eʙ"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units) - 1:  # Changed the condition to stop at the last unit
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])

@Client.on_callback_query(filters.regex(r'^start'))
async def start(bot, query):
    await query.message.edit_text(
        text=f"<b>Hᴇʟʟᴏ {query.from_user.mention}\n\nɪ ᴀᴍ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ᴇᴅɪᴛ ʙᴏᴛ ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.\n\nFᴏʀ ᴍᴏʀᴇ ɪɴғᴏ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.\n\nMᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ » <a href='https://t.me/Bot_Cracker'>Bᴏᴛ Cʀᴀᴄᴋᴇʀ 🎋</a>\n\n<spoiler>Cʀᴇᴅɪᴛ ɢᴏᴇs ᴛᴏ:- <a href='https://t.me/Mod_Moviez_X'>Mᴏᴅ Mᴏᴠɪᴇᴢ X ✨</a></spoiler></b>",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("⨭ Δᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇL ⨮", url=f"https://t.me/AutoCaption_Robot?startchannel=true")
            ],[
                InlineKeyboardButton("✭ Hᴇʟᴘ", callback_data="help"),
                InlineKeyboardButton("Aʙᴏᴜᴛ ✭", callback_data="about")
            ],[
                InlineKeyboardButton("⚝ Uᴘᴅᴀᴛᴇ", url=f"https://t.me/Bot_Cracker"),
                InlineKeyboardButton("Mᴏᴠɪᴇ ⚝", url=r"https://t.me/Mod_Moviez_X")
           ]]
        ),
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex(r'^help'))
async def help(bot, query):
    await query.message.edit_text(
        text=script.HELP_TXT,
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('✭ Aʙᴏᴜᴛ', callback_data='about')
            ],[
            InlineKeyboardButton('⇇ Bᴀᴄᴋ', callback_data='start')
            ]]
        ),
        disable_web_page_preview=True    
)


@Client.on_callback_query(filters.regex(r'^about'))
async def about(bot, query):
    await query.message.edit_text(
        text=script.ABOUT_TXT,
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('Hᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ?', callback_data='help')
            ],[
            InlineKeyboardButton('⇇ Bᴀᴄᴋ', callback_data='start')
            ]]
        ),
        disable_web_page_preview=True 

)
