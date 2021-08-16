#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ⭕️admin⭕️ : <a href='https://t.me/On_air_Filter_bot'>on air movies </a>\n\n○ movie searching Group : <a href='https://t.me/bhddhhddnjd'> ⭕️ Group ⭕️</a>\n\n○ ⭕️ Channel ⭕️ : <a href='https://t.me/on_air_movies'>⭕️👉click👈⭕️</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                
                    [
                        InlineKeyboardButton("❗️Close❗️", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
