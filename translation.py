# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper




import os
from config import Config

class Translation(object):
  START_TXT = """<b>Hᴇʏ {}

➻ I Aᴍ Δ Aᴅᴠᴀɴᴄᴇᴅ Aᴜᴛᴏ Fᴏʀᴡᴀʀᴅ Bᴏᴛ.
➻ I Cᴀɴ Fᴏʀᴡᴀʀᴅ Aʟʟ Mᴇꜱꜱᴀɢᴇꜱ Fʀᴏᴍ Cʜᴀɴɴᴇʟ To Aɴᴏᴛʜᴇʀ Cʜᴀɴɴᴇʟ 
➻ Cʟɪᴄᴋ Hᴇʟᴩ To Kɴᴏᴡ Moʀᴇ Aʙᴏᴜᴛ Mᴇ</b>"""


  HELP_TXT = """<b><u>⋈ Hᴇʟᴩ</b></u>

<b><u>≍ Aᴠᴀɪʟᴀʙʟᴇ Cᴏᴍᴍᴀɴᴅꜱ :</u></b>
⏣ __/start - Cʜᴇᴄᴋ I'ᴍ Aʟɪᴠᴇ__ 
⏣ __/forward - Fᴏʀᴡᴀʀᴅ Mᴇꜱꜱᴀɢᴇꜱ__
⏣ __/unequify - Dᴇʟᴇᴛᴇ Dᴜᴩʟɪᴄᴀᴛᴇ Mᴇꜱꜱᴀɢᴇꜱ Iɴ Cʜᴀɴɴᴇʟꜱ__
⏣ __/settings - Cᴏɴꜰɪɢᴜʀᴇ Yᴏᴜʀ Sᴇᴛᴛɪɴɢꜱ__
⏣ __/reset - Rᴇꜱᴇᴛ Yᴏᴜʀ Sᴇᴛᴛɪɴɢꜱ__

<b><u>≬≬ Fᴇᴀᴛᴜʀᴇꜱ :</b></u>
► __Fᴏʀᴡᴀʀᴅ Mᴇꜱꜱᴀɢᴇ Fʀᴏᴍ Pᴜʙʟɪᴄ Cʜᴀɴɴᴇʟ To Yᴏᴜʀ Cʜᴀɴɴᴇʟ Wɪᴛʜᴏᴜᴛ Aᴅᴍɪɴ Peᴇʀᴍɪꜱꜱɪᴏɴ. Iꜰ Tʜᴇ Cʜᴀɴɴᴇʟ Iꜱ Pʀɪᴠᴀᴛᴇ Nᴇᴇᴅ Aᴅᴍɪɴ Pᴇʀᴍɪꜱꜱɪᴏɴ, Bᴇᴛᴇʀ Tᴏ Uꜱᴇ UꜱᴇʀBᴏᴛ__
► __Forward Message Fʀᴏᴍ Private Cʜᴀɴɴᴇʟ To Yᴏᴜʀ Cʜᴀɴɴᴇʟ Bʏ Uꜱɪɴɢ UꜱᴇʀBᴏᴛ (Uꜱᴇʀ Mᴜꜱᴛ Bᴇ Mᴇᴍʙᴇʀ Iɴ Tʜᴇʀᴇ)__
► __Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ__
► __Cᴜꜱᴛᴏᴍ Bᴜᴛᴛᴏɴ__
► __Sᴜᴩᴩᴏʀᴛ Rᴇꜱᴛʀɪᴄᴛᴇᴅ Cʜᴀᴛꜱ__
► __Sᴋɪᴩ Dᴜᴩʟɪᴄᴀᴛᴇ Mᴇꜱꜱᴀɢᴇꜱ__
► __Fɪʟᴛᴇʀ Tʏᴩᴇ Oꜰ Mᴇꜱꜱᴀɢᴇꜱ__
► __Sᴋɪᴩ Mᴇꜱꜱᴀɢᴇꜱ Bᴀꜱᴇᴅ Oɴ Exᴛᴇɴꜱɪᴏɴꜱ & Kᴇʏᴡᴏʀᴅ & Sɪᴢᴇ__
"""
  
  HOW_USE_TXT = """<b><u>⚠️ Before Forwarding :</b></u>
  
► __Add A Bot Or Userbot__
► __Add Atleast One To Channel (Your Bot/Userbot Must Be Admin In There)__
► __You Can Add Chats Or Bots By Using /settings__
► __If The **From Channel** Is Private Your Userbot Must Be Member In There Or Your Bot Must Need Admin Permission In There Also__
► __Then Use /forward To Forward Messages__"""
  
  ABOUT_TXT = """<b>⋉ Mʏ Nᴀᴍᴇ :</b> {}
<b>⋉ Lᴀɴɢᴜᴀɢᴇ :</b> <a href='https://t.me/+0Zi1FC4ulo8zYzVl'>Sᴀᴍᴇ ᴀꜱ!</a>
<b>⋉ Lɪʙʀᴀʀʏ :</b> <a href='https://t.me/nt_Backup'>Bᴀᴄᴋ-Uᴩ 🕯️</a>
<b>⋉ Sᴇʀᴠᴇʀ :</b> <a href='https://t.me/+7P5-bLWSuPA5NmFl'>TG 🪄</a>
<b>⋉ Cʜᴀɴɴᴇʟ :</b> <a href='https://t.me/Bot_Cracker'>Bᴏᴛ Cʀᴀᴄᴋᴇʀ 🎶</a>
<b>⋉ Dᴇᴠᴇʟᴏᴩᴇʀ :</b> <a href='https://t.me/Syd_XyZ'>Jishu Developer</a>"""
  
  STATUS_TXT = """<b><u>Bᴏᴛ Sᴛᴀᴛᴜꜱ:</u></b>
  
<b>🎧 Tᴏᴛᴀʟ Uꜱᴇʀꜱ :</b> <code>{}</code>
<b>⚝ Tᴏᴛᴀʟ Bᴏᴛꜱ :</b> <code>{}</code>
<b>❉ Fᴏʀᴡᴀʀᴅɪɴɢ :</b> <code>{}</code>
"""
  
  FROM_MSG = "<b><u>Set Source Chat</></>\n\nForward The Last Message Or Last Message Link Of Source Chat.\n/cancel - To Cancel This Process"
  TO_MSG = "<b><u>Choose Target Chat</u></b>\n\nChoose Your Target Chat From The Given Buttons.\n/cancel - To Cancel This Process"
  SKIP_MSG = "<b><u>Set Message Skiping Number</u></b>\n\nSkip The Message As Much As You Enter The Number And The Rest Of The Message Will Be Forwarded\nDefault Skip Number = <code>0</code>\n<code>eg: You Enter 0 = 0 Message Skiped\nYou Enter 5 = 5 Message Skiped</code>\n/cancel - To Cancel This Process"
  CANCEL = "Process Cancelled Succefully !"
  BOT_DETAILS = "<b><u>📄 Bot Details</u></b>\n\n<b>➣ Name :</b> <code>{}</code>\n<b>➣ Bot ID :</b> <code>{}</code>\n<b>➣ Username :</b> @{}"
  USER_DETAILS = "<b><u>📄 UserBot Details</u></b>\n\n<b>➣ Name :</b> <code>{}</code>\n<b>➣ User ID :</b> <code>{}</code>\n<b>➣ Username :</b> @{}"  
         
  TEXT = """<b><u>Fᴏʀᴡᴀʀᴅ Sᴛᴀᴛᴜꜱ</u></b>
  
<b>🕵 Fᴇᴛᴄʜᴇᴅ Mᴇꜱꜱᴀɢᴇ :</b> <code>{}</code>
<b>✅ Sᴜᴄᴄᴇꜱꜰᴜʟʟʏ Fᴏʀᴡᴀʀᴅ :</b> <code>{}</code>
<b>👥 Dᴜʙʟɪᴄᴀᴛᴇ Mᴇꜱꜱᴀɢᴇ :</b> <code>{}</code>
<b>🗑 Dᴇʟᴇᴛᴇᴅ Mᴇꜱꜱᴀɢᴇ :</b> <code>{}</code>
<b>🪆 Sᴋɪᴩᴩᴇᴅ Mᴇꜱꜱᴀɢᴇ :</b> <code>{}</code>
<b>🔁 Fɪʟᴛᴇʀᴇᴅ Mᴇꜱꜱᴀɢᴇ :</b> <code>{}</code>
<b>📊 Cᴜʀʀᴇɴᴛ Sᴛᴀᴛᴜꜱ :</b> <code>{}</code>
<b>🔥 Pᴇʀᴄᴇɴᴛᴀɢᴇ :</b> <code>{}</code> %

{}
"""

  TEXT1 = """<b><u>Fᴏʀᴡᴀʀᴅ Sᴛᴀᴛᴜꜱ</u></b>

<b>🕵 Fᴇᴛᴄʜᴇᴅ Mᴇꜱꜱᴀɢᴇ :</b> <code>{}</code>
<b>✅ Sᴜᴄᴄᴇꜱꜰᴜʟʟʏ Fᴏʀᴡᴀʀᴅ :</b> <code>{}</code>
<b>👥 Dᴜʙʟɪᴄᴀᴛᴇ Mᴇꜱꜱᴀɢᴇ :</b> <code>{}</code>
<b>🗑 Dᴇʟᴇᴛᴇᴅ Mᴇꜱꜱᴀɢᴇ :</b> <code>{}</code>
<b>🪆 Sᴋɪᴩᴩᴇᴅ Mᴇꜱꜱᴀɢᴇ :</b> <code>{}</code>
<b>📊 Sᴛᴀᴛꜱ :</b> <code>{}</code>
<b>⏳ Pʀᴏɢʀᴇꜱꜱ :</b> <code>{}</code>
<b>⏰ Eᴛᴀ :</b> <code>{}</code>
{}"""

  DUPLICATE_TEXT = """<b><u>Unequify Status</u></b>

<b>🕵 Fetched Files :</b> <code>{}</code>

<b>👥 Dublicate Deleted :</b> <code>{}</code>

{}
"""
  DOUBLE_CHECK = """<b><u>Double Checking</u></b>
  
Before Forwarding The Messages Click The Yes Button Only After Checking The Following

<b>★ Your Bot :</b> [{botname}](t.me/{botuname})
<b>★ From Channel :</b> <code>{from_chat}<>
<b>★ To Channel :</b> <code>{to_chat}</code>
<b>★ Skip Messages :</b> <code>{skip}</code>

<i>° [{botname}](t.me/{botuname}) Must Be Admin In <b>Target Chat</b></i> (<code>{to_chat}</code>)
<i>° If The <b>Source Chat</b> Is Private Your Userbot Must Be Member Or Your Bot Must Be Admin In There Also</i>

<b>If The Above Is Checked Then The Yes Button Can Be Clicked</b>"""










# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
