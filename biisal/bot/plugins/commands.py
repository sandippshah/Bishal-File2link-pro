# (c) @biisal @adarsh

from biisal.bot import StreamBot
from pyrogram import Client, filters
from biisal.vars import Var
import logging
logger = logging.getLogger(__name__)
from biisal.bot.plugins.stream import MY_PASS
from biisal.utils.human_readable import humanbytes
from biisal.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from biisal.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup
from biisal.vars import bot_name , bisal_channel , bisal_grp
from biisal.utils.a_utils import check_verification, get_token, verify_user, check_token


SRT_TXT = """<b>ᴊᴀɪ sʜʀᴇᴇ ᴋʀsɴᴀ {}!,
I ᴀᴍ Fɪʟᴇ ᴛᴏ Lɪɴᴋ Gᴇɴᴇʀᴀᴛᴏʀ Bᴏᴛ ᴡɪᴛʜ Cʜᴀɴɴᴇʟ sᴜᴘᴘᴏʀᴛ.

Sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ ᴀɴᴅ ɢᴇᴛ ᴀ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ ᴀɴᴅ sᴛʀᴇᴀᴍᴀʙʟᴇ ʟɪɴᴋ.!
ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='http://telegram.me/spshah878/'>Shaho</a></b>"""

@StreamBot.on_message(filters.command("start") & filters.private)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.NEW_USER_LOG,
            f"**New User Joined:** \n\n__My new friend__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __started your bot!__\nBot : @{Var.BOT_USERNAME}"
        )

    data = m.text.split()
    if len(data) > 1 and data[1].split("-", 1)[0] == "verify":
        userid = data[1].split("-", 2)[1]
        token = data[1].split("-", 3)[2]
        if str(m.from_user.id) != str(userid):
            return await m.reply_text(
                text="<b>Invalid link or Expired link!</b>",
                protect_content=True
            )
        is_valid = await check_token(b, userid, token)
        if is_valid:
            await verify_user(b, userid, token)
            await m.reply_text(
                text=f"<b>Hey {m.from_user.mention}, You are successfully verified!\nNow you have unlimited access for Streaming and Downloading Movies for 12 hours</b>",
                protect_content=True
            )
            # Send log message to V_LOG_CHANNEL after successful verification
            await b.send_message(
                Var.V_LOG_CHANNEL,
                f"**New User Verified:** \n\n__My new friend__ [{m.from_user.first_name}](tg://user?id={m.from_user.id})\nBot : @{Var.BOT_USERNAME}"
            )
        else:
            return await m.reply_text(
                text="<b>Invalid link or Expired link!</b>",
                protect_content=True
            )
        return  # Return early after handling verification

    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="__Sorry, you are banned from using me. Contact the developer for help.__",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://graph.org/file/28dad3c3aea3cad735a6e.jpg",
                caption="<b>Hᴇʏ ᴛʜᴇʀᴇ!\n\nPʟᴇᴀsᴇ ɪᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ! \n😊 Dᴜᴇ ᴛᴏ sᴇʀᴠᴇʀ ᴏᴠᴇʀʟᴏᴀᴅ.\nᴏɴʟʏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ!</b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Join now 🚩", url=f"https://t.me/{Var.UPDATES_CHANNEL}")]
                    ]
                )
            )
            return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<b>Something went wrong. Please <a href='http://telegram.me/spshah878/'>click here for support</a></b>",
                disable_web_page_preview=True
            )
            return

    await StreamBot.send_photo(
        chat_id=m.chat.id,
        photo="https://graph.org/file/28dad3c3aea3cad735a6e.jpg",
        caption=SRT_TXT.format(m.from_user.mention(style="md")),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Update Channel 🤡", url="http://telegram.me/Rx_Bots/")],
                [
                    InlineKeyboardButton("About 😎", callback_data="about"),
                    InlineKeyboardButton("Help 😅", callback_data="help")
                ],
                [InlineKeyboardButton("Our Group 🚩", url="https://t.me/+lphQvs9EC7hiNTZl")],
                [
                    InlineKeyboardButton("Disclaimer 🔻", url="https://t.me/pikashow_Movies_Update/43"),
                    InlineKeyboardButton("Dev 😊", callback_data="aboutDev")
                ]
            ]
        )
    )
@StreamBot.on_message(filters.command("help") & filters.private )
async def help_cd(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.NEW_USER_LOG,
            f"**New User Joined:** \n\n__My new friend__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __started your bot!__\nBot : @{Var.BOT_USERNAME}"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="__𝓢𝓞𝓡𝓡𝓨, 𝓨𝓞𝓤 𝓐𝓡𝓔 𝓐𝓡𝓔 𝓑𝓐𝓝𝓝𝓔𝓓 𝓕𝓡𝓞𝓜 𝓤𝓢𝓘𝓝𝓖 𝓜𝓔. 𝓒ᴏɴᴛᴀᴄᴛ ᴛʜᴇ 𝓓ᴇᴠᴇʟᴏᴘᴇʀ__\n\n  **𝙃𝙚 𝙬𝙞𝙡𝙡 𝙝𝙚𝙡𝙥 𝙮𝙤𝙪**",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://graph.org/file/28dad3c3aea3cad735a6e.jpg",
                caption=""""<b>Hᴇʏ ᴛʜᴇʀᴇ!\n\nPʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ ! 😊\n\nDᴜᴇ ᴛᴏ sᴇʀᴠᴇʀ ᴏᴠᴇʀʟᴏᴀᴅ, ᴏɴʟʏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ !</b>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jᴏɪɴ ɴᴏᴡ 🚩", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<b>sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ.ᴘʟᴇᴀsᴇ <a href='http://telegram.me/spshah878/'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ sᴜᴘᴘᴏʀᴛ</a></b>",
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
    chat_id=m.chat.id,
    photo="https://graph.org/file/28dad3c3aea3cad735a6e.jpg",
    caption=f"<b>ᴡᴇ ᴅᴏɴᴛ ɴᴇᴇᴅ ᴍᴀɴʏ <a href='http://telegram.me/Rx_Bots/'>ᴄᴏᴍᴍᴀɴᴅs</a> ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ 🤩.\n\nᴊᴜsᴛ sᴇɴᴅ ᴍᴇ <a href='http://telegram.me/Rx_Bots/'>ᴠɪᴅᴇᴏ ғɪʟᴇs</a> ᴀɴᴅ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ <a href='http://telegram.me/Rx_Bots/'>ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ & sᴛʀᴇᴀᴍᴀʙʟᴇ</a> ʟɪɴᴋ.\n\nᴏʀ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ɪɴ <a href='http://telegram.me/Rx_Bots/'>ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ</a>..ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴀɴᴅ sᴇᴇ ᴍʏ ᴍᴀɢɪᴄ 😎</b>",
    reply_markup=InlineKeyboardMarkup(
        [
            [   
                InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ 🤡", url=f"http://telegram.me/Rx_Bots/")
            ],
            [
                InlineKeyboardButton("ᴅɪsᴄʟᴀɪᴍᴇʀ 🔻", url=f"https://t.me/pikashow_Movies_Update/43"),
                InlineKeyboardButton("ᴏᴜʀ ɢʀᴏᴜᴘ 🚩", url=f"https://t.me/+lphQvs9EC7hiNTZl"),

            ],
            [
                InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="start"),

            ]

        ]
    )
)
@StreamBot.on_message(filters.command('ban') & filters.user(Var.OWNER_ID))
async def do_ban(bot ,  message):
    userid = message.text.split(" ", 2)[1] if len(message.text.split(" ", 1)) > 1 else None
    reason = message.text.split(" ", 2)[2] if len(message.text.split(" ", 2)) > 2 else None
    if not userid:
        return await message.reply('<b>ᴘʟᴇᴀsᴇ ᴀᴅᴅ ᴀ ᴠᴀʟɪᴅ ᴜsᴇʀ/ᴄʜᴀɴɴᴇʟ ɪᴅ ᴡɪᴛʜ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ\n\nᴇx : /ban (user/channel_id) (banning reason[Optional]) \nʀᴇᴀʟ ᴇx : <code>/ban 1234567899</code>\nᴡɪᴛʜ ʀᴇᴀsᴏɴ ᴇx:<code>/ban 1234567899 seding adult links to bot</code>\nᴛᴏ ʙᴀɴ ᴀ ᴄʜᴀɴɴᴇʟ :\n<code>/ban CHANEL_ID</code>\nᴇx : <code>/ban -1001234567899</code></b>')
    text = await message.reply("<b>ʟᴇᴛ ᴍᴇ ᴄʜᴇᴄᴋ 👀</b>")
    banSts = await db.ban_user(userid)
    if banSts == True:
        await text.edit(
    text=f"<b><code>{userid}</code> ʜᴀs ʙᴇᴇɴ ʙᴀɴɴᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ\n\nSʜᴏᴜʟᴅ I sᴇɴᴅ ᴀɴ ᴀʟᴇʀᴛ ᴛᴏ ᴛʜᴇ ʙᴀɴɴᴇᴅ ᴜsᴇʀ?</b>",
    reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ʏᴇs ✅", callback_data=f"sendAlert_{userid}_{reason if reason else 'no reason provided'}"),
                InlineKeyboardButton("ɴᴏ ❌", callback_data=f"noAlert_{userid}"),
            ],
        ]
    ),
)
    else:
        await text.edit(f"<b>Cᴏɴᴛʀᴏʟʟ ʏᴏᴜʀ ᴀɴɢᴇʀ ʙʀᴏ...\n<code>{userid}</code> ɪs ᴀʟʀᴇᴀᴅʏ ʙᴀɴɴᴇᴅ !!</b>")
    return


@StreamBot.on_message(filters.command('unban') & filters.user(Var.OWNER_ID))
async def do_unban(bot ,  message):
    userid = message.text.split(" ", 2)[1] if len(message.text.split(" ", 1)) > 1 else None
    if not userid:
        return await message.reply('ɢɪᴠᴇ ᴍᴇ ᴀɴ ɪᴅ\nᴇx : <code>/unban 1234567899<code>')
    text = await message.reply("<b>ʟᴇᴛ ᴍᴇ ᴄʜᴇᴄᴋ 🥱</b>")
    unban_chk = await db.is_unbanned(userid)
    if  unban_chk == True:
        await text.edit(text=f'<b><code>{userid}</code> ɪs ᴜɴʙᴀɴɴᴇᴅ\nSʜᴏᴜʟᴅ I sᴇɴᴅ ᴛʜᴇ ʜᴀᴘᴘʏ ɴᴇᴡs ᴀʟᴇʀᴛ ᴛᴏ ᴛʜᴇ ᴜɴʙᴀɴɴᴇᴅ ᴜsᴇʀ?</b>',
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("ʏᴇs ✅", callback_data=f"sendUnbanAlert_{userid}"),
                InlineKeyboardButton("ɴᴏ ❌", callback_data=f"NoUnbanAlert_{userid}"),
            ],
        ]
    ),
)

    elif unban_chk==False:
        await text.edit('<b>ᴜsᴇʀ ɪs ɴᴏᴛ ʙᴀɴɴᴇᴅ ʏᴇᴛ.</b>')
    else :
        await text.edit(f"<b>ғᴀɪʟᴇᴅ ᴛᴏ ᴜɴʙᴀɴ ᴜsᴇʀ/ᴄʜᴀɴɴᴇʟ.\nʀᴇᴀsᴏɴ : {unban_chk}</b>")


@StreamBot.on_callback_query()
async def cb_handler(client, query):
    data = query.data
    if data == "close_data":
        await query.message.delete()

    elif data == "start":
        await query.message.edit_caption(
            caption=SRT_TXT.format(query.from_user.mention(style="md")),
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ 🤡", url="http://telegram.me/Rx_Bots/")],
                    [
                        InlineKeyboardButton("ᴀʙᴏᴜᴛ 😎", callback_data="about"),
                        InlineKeyboardButton("ʜᴇʟᴘ 😅", callback_data="help")
                    ],
                    [InlineKeyboardButton("ᴏᴜʀ ɢʀᴏᴜᴘ 🚩", url="https://t.me/+lphQvs9EC7hiNTZl")],
                    [
                        InlineKeyboardButton("ᴅɪsᴄʟᴀɪᴍᴇʀ 🔻", url="https://t.me/pikashow_Movies_Update/43"),
                        InlineKeyboardButton("ᴅᴇᴠ 😊", callback_data="aboutDev")
                    ]
                ]
            )
        )

    elif data == "about":
        await query.message.edit_caption(
            caption=(
                f"<b>Mʏ ɴᴀᴍᴇ :<a href='http://telegram.me/Pikashow_File2Link_Bot/'>{bot_name}</a>\n"
                f"Aᴅᴍɪɴ : <a href='http://telegram.me/spshah878/'>S.p.Shah</a>\n"
                "ʜᴏsᴛᴇᴅ ᴏɴ : ʜᴇʀᴏᴋᴜ\n"
                "ᴅᴀᴛᴀʙᴀsᴇ : ᴍᴏɴɢᴏ ᴅʙ\n"
                "ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ 3</b>"
            ),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="start"),
                        InlineKeyboardButton("ᴄʟᴏsᴇ ‼️", callback_data="close_data")
                    ]
                ]
            )
        )
    elif data == "help":
        await query.message.edit_caption(
            caption=(
                f"<b>ᴡᴇ ᴅᴏɴᴛ ɴᴇᴇᴅ ᴍᴀɴʏ <a href='https://t.me/pikashow_Movies_Update/43'>ᴄᴏᴍᴍᴀɴᴅs</a> ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ 🤩.\n\n"
                "ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ <a href='http://telegram.me/Rx_Bots/'>ᴠɪᴅᴇᴏ ғɪʟᴇs</a> ᴀɴᴅ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ "
                "<a href='http://telegram.me/Pikashow_File2Link_Bot/'>ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ & sᴛʀᴇᴀᴍᴀʙʟᴇ</a> ʟɪɴᴋ.\n\n"
                "ᴏʀ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ɪɴ <a href='http://t.me/Pikashow_File2Link_Bot?startgroup=true'>ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ</a>.."
                "ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴀɴᴅ sᴇᴇ ᴍʏ ᴍᴀɢɪᴄ 😎</b>"
            ),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="start"),
                        InlineKeyboardButton("ᴄʟᴏsᴇ ‼️", callback_data="close_data")
                    ]
                ]
            )
        )

    elif data == "aboutDev":
        await query.message.edit_caption(
            caption=(
                f"<b>ᴊᴀɪ sʜʀᴇᴇ ᴋʀsɴᴀ ᴅᴇᴀʀ...\n"
                f"ɪᴍ <a href='http://telegram.me/spshah/'>S.p.Shah</a>\n"
                "ɪ ᴀᴍ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏғ ᴛʜɪs ʙᴏᴛ</b>"
            ),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="start"),
                        InlineKeyboardButton("ᴄʟᴏsᴇ ‼️", callback_data="close_data")
                    ]
                ]
            )
        )
    elif data.startswith("sendAlert"):
        user_id = data.split("_")[1]
        user_id = int(user_id.replace(' ', ''))
        if len(str(user_id)) == 10:
            reason = str(data.split("_")[2])
            try:
                await client.send_message(user_id, f'<b>ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ʙʏ ᴀᴅᴍɪɴ.\nRᴇᴀsᴏɴ : {reason}</b>')
                await query.message.edit(f"<b>Aʟᴇʀᴛ sᴇɴᴛ ᴛᴏ <code>{user_id}</code>\nRᴇᴀsᴏɴ : {reason}</b>")
            except Exception as e:
                await query.message.edit(f"<b>sʀʏ ɪ ɢᴏᴛ ᴛʜɪs ᴇʀʀᴏʀ : {e}</b>")
        else:
            await query.message.edit(f"<b>Tʜᴇ ᴘʀᴏᴄᴇss ᴡᴀs ɴᴏᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ʙᴇᴄᴀᴜsᴇ ᴛʜᴇ ᴜsᴇʀ ɪᴅ ᴡᴀs ɴᴏᴛ ᴠᴀʟɪᴅ, ᴏʀ ᴘᴇʀʜᴀᴘs ɪᴛ ᴡᴀs ᴀ ᴄʜᴀɴɴᴇʟ ɪᴅ</b>")

    elif data.startswith("noAlert"):
        user_id = data.split("_")[1]
        user_id = int(user_id.replace(' ', ''))
        await query.message.edit(f"<b>Tʜᴇ ʙᴀɴ ᴏɴ <code>{user_id}</code> ᴡᴀs ᴇxᴇᴄᴜᴛᴇᴅ sɪʟᴇɴᴛʟʏ.</b>")

    elif data.startswith("sendUnbanAlert"):
        user_id = data.split("_")[1]
        user_id = int(user_id.replace(' ', ''))
        if len(str(user_id)) == 10:
            try:
                unban_text = '<b>ʜᴜʀʀᴀʏ..ʏᴏᴜ ᴀʀᴇ ᴜɴʙᴀɴɴᴇᴅ ʙʏ ᴀᴅᴍɪɴ.</b>'
                await client.send_message(user_id, unban_text)
                await query.message.edit(f"<b>Uɴʙᴀɴɴᴇᴅ Aʟᴇʀᴛ sᴇɴᴛ ᴛᴏ <code>{user_id}</code>\nᴀʟᴇʀᴛ ᴛᴇxᴛ : {unban_text}</b>")
            except Exception as e:
                await query.message.edit(f"<b>sʀʏ ɪ ɢᴏᴛ ᴛʜɪs ᴇʀʀᴏʀ : {e}</b>")
        else:
            await query.message.edit(f"<b>Tʜᴇ ᴘʀᴏᴄᴇss ᴡᴀs ɴᴏᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ʙᴇᴄᴀᴜsᴇ ᴛʜᴇ ᴜsᴇʀ ɪᴅ ᴡᴀs ɴᴏᴛ ᴠᴀʟɪᴅ, ᴏʀ ᴘᴇʀʜᴀᴘs ɪᴛ ᴡᴀs ᴀ ᴄʜᴀɴɴᴇʟ ɪᴅ</b>")

    elif data.startswith("NoUnbanAlert"):
        user_id = data.split("_")[1]
        user_id = int(user_id.replace(' ', ''))
        await query.message.edit(f"Tʜᴇ ᴜɴʙᴀɴ ᴏɴ <code>{user_id}</code> ᴡᴀs ᴇxᴇᴄᴜᴛᴇᴅ sɪʟᴇɴᴛʟʏ.")






 