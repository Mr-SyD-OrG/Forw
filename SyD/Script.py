import os

class script(object):

    START_TXT = """<b>Hᴇʟʟᴏ {}\n\n
ɪ ᴀᴍ ᴛʜᴇ ᴍᴏꜱᴛ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ᴡɪᴛʜ ᴘʀᴇᴍɪᴜᴍ ꜰᴇᴀᴛᴜʀᴇꜱ, ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ cʜᴀɴɴᴇʟ ᴀɴᴅ ᴇɴᴊᴏʏ

‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/Mrkillerdeveloper'>Mʀᴋɪʟʟᴇʀ Dᴇᴠᴇʟᴏᴘᴇʀ</a></b>
"""

    HELP_TXT = """⚹ Hᴇʟᴩ Txᴛ, Fᴏʀ Uꜱɪɴɢ Mᴇ

• Aᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ ғᴜʟʟ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.
• Usᴇ ᴄᴏᴍᴍᴀɴᴅ ɢɪᴠᴇ ʙᴇʟᴏᴡ ɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ.
• Tʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋ ɪɴ ᴄʜᴀɴɴᴇʟ.
• Kᴇᴇᴘ ғɪʟᴇ ᴡɪᴛʜᴏᴜᴛ ғᴏʀᴡᴀʀᴅ ᴛᴀɢ.

•> /set_cap - Sᴇᴛ Nᴇᴡ Cᴀᴘᴛɪᴏɴ Iɴ ʏᴏᴜʀ Cʜᴀɴɴᴇʟ
•> /see_cap - Sᴇᴇ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ
•> /del_cap - Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ

❉ Fᴏʀᴍᴀᴛ; 

`{file_name}` = Oʀɪɢɪɴᴀʟ Fɪʟᴇ Nᴀᴍᴇ
`{file_size}` = Oʀɪɢɪɴᴀʟ Fɪʟᴇ Sɪᴢᴇ 
`{language}` = Lᴀɴɢᴜᴀɢᴇ Oғ Fɪʟᴇ Nᴀᴍᴇ
`{year}` = Yᴇᴀʀ Oғ Fɪʟᴇ
`{default_caption}` = Rᴇᴀʟ Cᴀᴘᴛɪᴏɴ Oғ Fɪʟᴇ.

Eg:- `/set_cap
{file_name}

⚙️ Size » {file_size}

╔═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╗
💥 𝙅𝙊𝙄𝙉 :- ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ 
💥 𝙅𝙊𝙄𝙉 :- ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ
╚═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╝`
"""

    ABOUT_TXT = """<b>╔════❰ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ᴇᴅɪᴛ ʙᴏᴛ ❱═❍⊱❁
║╭━━━━━━━━━━━━━━━➣
║┣⪼Bᴏᴛ : <a href='https://t.me/Auto_Caption_Edit_bot'>ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ᴇᴅɪᴛ ʙᴏᴛ</a>
║┣⪼Cʀᴇᴀᴛᴏʀ : <a href='https://t.me/Syd_Xyz'>Mʀ Sʏᴅ ✨</a>
║┣⪼Uᴘᴅᴀᴛᴇ : <a href='https://t.me/Bot_Cracker'>Bᴏᴛ Cʀᴀᴄᴋᴇʀ 🎋 ™</a>
║┣⪼Hᴏsᴛᴇᴅ ᴏɴ : TG
║┣⪼Lᴀɴɢᴜᴀɢᴇ : Sᴀᴍᴇ ᴀꜱ ʏᴏᴜʀꜱ
║┣⪼Lɪʙʀᴀʀʏ : Tᴇʟᴇɢʀᴀᴍ
║┣⪼Vᴇʀsɪᴏɴ : 1.0.0 [ᴍᴏsᴛ sᴛᴀʙʟᴇ]
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁</b>"""
