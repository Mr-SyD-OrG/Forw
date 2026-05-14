
import re
import asyncio 
from .utils import STS
from database import db
from config import temp 
from translation import Translation
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.errors.exceptions.not_acceptable_406 import ChannelPrivate as PrivateChat
from pyrogram.errors.exceptions.bad_request_400 import ChannelInvalid, ChatAdminRequired, UsernameInvalid, UsernameNotModified, ChannelPrivate
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
 
SYD_CHANNELS = ["Bot_Cracker", "Mod_Moviez_X", "MrSyD_Tg"]
PREMIUM = [1733124290, 8796242071]
# async def not_subscribed(_, __, message):
    #for channel in SYD_CHANNELS:
       # try:
           # user = await message._client.get_chat_member(channel, message.from_user.id)
          #  if user.status in {"kicked", "left"}:
           #     return True
      #  except UserNotParticipant:
          #  return True
#    return False
#===================Run Function===================#

@Client.on_message(filters.private & filters.command(["fwd", "forward"]))
async def run(bot, message):
    buttons = []
    btn_data = {}
    user_id = message.from_user.id
    _bot = await db.get_bot(user_id)
    if not _bot:
      return await message.reply("Yᴏᴜ Dɪᴅ Nᴏᴛ Aᴅᴅᴇᴅ Aɴʏ Bᴏᴛ. Pʟᴇᴀꜱᴇ Aᴅᴅ A Bᴏᴛ Uꜱɪɴɢ /settings !")
    channels = await db.get_user_channels(user_id)
    if not channels:
       return await message.reply_text("Please Set A To Channel In /settings Before Forwarding")
    not_joined_channels = []
    for channel in SYD_CHANNELS:
        try:
            user = await bot.get_chat_member(channel, message.from_user.id)
            if user.status in {"kicked", "left"}:
                not_joined_channels.append(channel)
        except UserNotParticipant:
            not_joined_channels.append(channel)
            
    if not_joined_channels:
        buttons = [
            [
                InlineKeyboardButton(
                    text=f"✧ Jᴏɪɴ {channel.capitalize().replace("_", " ")}✧", url=f"https://t.me/{channel}"
                )
            ]
        for channel in not_joined_channels
        ]
        buttons.append(
            [
                InlineKeyboardButton(
                    text="✧ Jᴏɪɴ Bᴀᴄᴋ Uᴩ ✧", url="https://t.me/+0Zi1FC4ulo8zYzVl"

                )
            ]
        )
        buttons.append(
            [
                InlineKeyboardButton(
                    text="☑ ᴊᴏɪɴᴇᴅ ☑", callback_data="check_subscription"
                )
            ]
        )

        text = "**Sᴏʀʀʏ, ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴊᴏɪɴ ɪɴ ᴏᴜʀ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟꜱ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ꜰᴇᴀᴛᴜʀᴇ, ᴩʟᴇᴀꜱᴇ ᴅᴏ ꜱᴏ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ,,... ⚡ .**"
        return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
        
    if len(channels) > 1:
       for channel in channels:
          buttons.append([KeyboardButton(f"{channel['title']}")])
          btn_data[channel['title']] = channel['chat_id']
       buttons.append([KeyboardButton("cancel")]) 
       _toid = await bot.ask(message.chat.id, Translation.TO_MSG.format(_bot['name'], _bot['username']), reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True, resize_keyboard=True))
       if _toid.text.startswith(('/', 'cancel')):
          return await message.reply_text(Translation.CANCEL, reply_markup=ReplyKeyboardRemove())
       to_title = _toid.text
       toid = btn_data.get(to_title)
       if not toid:
          return await message.reply_text("Wrong Channel Choosen !", reply_markup=ReplyKeyboardRemove())
    else:
       toid = channels[0]['chat_id']
       to_title = channels[0]['title']
    fromid = await bot.ask(message.chat.id, Translation.FROM_MSG, reply_markup=ReplyKeyboardRemove())
    if fromid.text and fromid.text.startswith('/'):
        await message.reply(Translation.CANCEL)
        return 
    if fromid.text and not fromid.forward_date:
        regex = re.compile(r"(https://)?(t\.me/|telegram\.me/|telegram\.dog/)(c/)?(\d+|[a-zA-Z_0-9]+)/(\d+)$")
        match = regex.match(fromid.text.replace("?single", ""))
        if not match:
            return await message.reply('Invalid Link')
        chat_id = match.group(4)
        last_msg_id = int(match.group(5))
        if chat_id.isnumeric():
            chat_id  = int(("-100" + chat_id))
    elif fromid.forward_from_chat.type in [enums.ChatType.CHANNEL]:
        last_msg_id = fromid.forward_from_message_id
        chat_id = fromid.forward_from_chat.username or fromid.forward_from_chat.id
        if last_msg_id == None:
           return await message.reply_text("This May Be A Forwarded Message From A Group And Sended By Anonymous Admin. Instead Of This Please Send Last Message Link From Group")
    else:
        await message.reply_text("Invalid !")
        return 
    sydtxt = "Oɴʟʏ Fᴏʀ Pʀᴇᴍɪᴜᴍ Uꜱᴇʀꜱ, Tᴏ Bᴜʏ : /buy"
    if message.chat.id in PREMIUM:
        replyto = await bot.ask(message.chat.id, Translation.REPLY_MSG, reply_markup=ReplyKeyboardRemove())
        if replyto.text and replyto.text.startswith('/'):
            await message.reply(Translation.CANCEL)
            return
        if replyto.text:
            try:
                syd = int(replyto.text)
            except ValueError:
                syd = 0
                await message.reply_text("Invalid reply id! Skipping feature.")
        else:
            syd = 0
            await message.reply_text("Invalid ! Skipping Feature")
        sydtxt = f"{syd} 🌿"
    try:
        title = (await bot.get_chat(chat_id)).title
  #  except ChannelInvalid:
        #return await fromid.reply("**Given source chat is copyrighted channel/group. you can't forward messages from there**")
    except (PrivateChat, ChannelPrivate, ChannelInvalid):
        title = "private" if fromid.text else fromid.forward_from_chat.title
    except (UsernameInvalid, UsernameNotModified):
        return await message.reply('Invalid Link Specified.')
    except Exception as e:
        return await message.reply(f'Errors - {e}')
    skipno = await bot.ask(message.chat.id, Translation.SKIP_MSG)
    if skipno.text.startswith('/'):
        await message.reply(Translation.CANCEL)
        return
    forward_id = f"{user_id}-{skipno.id}"
    buttons = [[
        InlineKeyboardButton('Yᴇꜱ', callback_data=f"start_public_{forward_id}"),
        InlineKeyboardButton('Nᴏ', callback_data="close_btn")
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(
        text=Translation.DOUBLE_CHECK.format(botname=_bot['name'], botuname=_bot['username'], from_chat=title, to_chat=to_title, skip=skipno.text, syd=sydtxt),
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )
    
    STS(forward_id).store(chat_id, toid, int(skipno.text), int(last_msg_id), int(syd))




@Client.on_callback_query(filters.regex("check_subscription"))
async def check_subscription(client, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    not_joined_channels = []

    for channel in SYD_CHANNELS:
        try:
            user = await client.get_chat_member(channel, user_id)
            if user.status in {"kicked", "left"}:
                not_joined_channels.append(channel)
        except UserNotParticipant:
            not_joined_channels.append(channel)

    if not not_joined_channels:
        await callback_query.message.edit_text(
            "**Tʜᴀɴᴋꜱ ✨, Yᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ ᴏɴ ᴀʟʟ ᴛʜᴇ ʀᴇqᴜɪʀᴇᴅ ᴄʜᴀɴɴᴇʟꜱ. \nCʟɪᴄᴋ ᴏɴ 😊 /forward ɴᴏᴡ ᴛᴏ ꜱᴛᴀʀᴛ ᴛʜᴇ ᴩʀᴏᴄᴇꜱꜱ.....⚡**"
        )
        await callback_query.message.reply("🎊")
    else:
        buttons = [
            [
                InlineKeyboardButton(
                    text=f"✧ Jᴏɪɴ {channel.capitalize().replace("_", " ")} ✧",
                    url=f"https://t.me/{channel}",
                )
            ]
            for channel in not_joined_channels
        ]
        buttons.append(
            [
                InlineKeyboardButton(
                    text="✧ Jᴏɪɴ Bᴀᴄᴋ Uᴩ ✧", url="https://t.me/+0Zi1FC4ulo8zYzVl"

                )
            ]
        )

        buttons.append(
            [
                InlineKeyboardButton(
                    text="☑ ᴊᴏɪɴᴇᴅ ☑", callback_data="check_subscription"
                )
            ]
        )

        text = "**Sᴛɪʟʟ 🥲, ʏᴏᴜ ʜᴀᴠᴇɴᴛ ᴊᴏɪɴᴇᴅ ɪɴ ᴏᴜʀ ᴀʟʟ ʀᴇqᴜɪʀᴇᴅ ᴄʜᴀɴɴᴇʟꜱ, ᴩʟᴇᴀꜱᴇ ᴅᴏ ꜱᴏ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ..✨ .**"
        await callback_query.message.edit_text(
            text=text, reply_markup=InlineKeyboardMarkup(buttons)
     )

