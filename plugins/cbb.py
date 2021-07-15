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
            text = f"<b>○ Master : <a href='https://t.me/DARK_ANGEL_1234'>THIS_PERSONAL</a>\n<b>○ Group : <a href='https://t.me/Fantasy_Worldz'>FANTASY_WORLD</a>\n<b>○ Channel : <a href='https://t.me/Fantasy_Movies'>FANTASY_MOVIES</a>\n<b>○ Channel : <a href='https://t.me/Fantasy_Seriesz'>FANTASY_SERIES</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
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
