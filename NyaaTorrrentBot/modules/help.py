from NyaaTorrrentBot import NYAA, botname
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

HELP_TEXT = """
**Note:** The bot will fetch some of the recent torrents, so be specific with search query.

**Available Commands:**
- /start - To check whether the bot is alive.
- /help - To display this message.
- /magnet - To get torrent info from **Nyaa** Using ID.

**searching on [Nyaa](https://nyaa.si)**:
- /anime - Anime torrents.
- /manga - Manga torrents.
- /audio - Audio/Soundtrack torrents.
- /live_action - Live Action shows/movies torrents.
- /pictures - Picturebook/Graphics torrents.
- /software - Games/Applications torrents.

**Examples:**
**/anime Attack on Titan**
**/magnet 1234567**
"""

ABOUT_TEXT = """
Made with ❤️ by @AmiFutami
"""

@NYAA.on_message(filters.command(["help", f"help@{botname}"], prefixes = "/") & ~filters.edited)
async def help(client, message):
    await NYAA.send_message(chat_id = message.chat.id, text = HELP_TEXT, disable_web_page_preview = True)

@NYAA.on_message(filters.command(["about", f"about@{botname}"], prefixes = "/") & ~filters.edited)
async def about(client, message):
    buttons = [
                [InlineKeyboardButton("Bot Dev?", url = "https://t.me/AmiFutami"), InlineKeyboardButton("Report Issues", url = "https://t.me/CapitalLondonRadio")]
              ]
    await NYAA.send_message(chat_id = message.chat.id, text = ABOUT_TEXT, reply_markup = InlineKeyboardMarkup(buttons))
