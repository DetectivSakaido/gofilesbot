# ----------------------------------- https://github.com/m4mallu/gofilesbot ------------------------------------------ #

class Presets(object):
    CAPTION_TEXT_DOC = "\n\n<b>File Name:</b> {}\n\n<b>Format:</b> {}\n<b>Size:</b> {}"
    CAPTION_TEXT_VID = "\n\n<b>File Name:</b> {}\n\n<b>Size:</b> {}"
    ASK_PM_TEXT = "<b>Click the below button</b>"
    WELCOME_TEXT = "Hello.. <b>{}</b>\n<code>I can help you getting anime music tracks from</code> @animemusicstashgroup. "
                 
    CLEAN_CHAT_MSG = "⚠️ <b>Deleting all messages..</b>"
    MSG_FOR_PIN = "<b>For getting medias from here..</b>\n\n🔛 <code>Please start</code> @{} <code>in PM\n\n" \
                  "Send the exact music name.\n\n🔊 I'll reply the file in PM if available in our channel !</code>"

    BOT_PM_TEXT = "<b>Sorry.. 😢</b>\n\n<code>Bot won't work in PM, Ask in ma Group. I'll reply the file in PM if " \
                  "available in our DB !</code>"
    PM_ERROR = "<b>Unable to send medias</b> ⛔️\n<code>Click the below button\nAsk here for files later!</code>"
    MEDIA_SEND_TEXT = "<code>Media dispatched as PM 🥳</code>"
    NO_MEDIA = "Requested Music track: <b>{}</b>\n\n<b>Not available " \
               "Right Now</b>\n<code>Possible Causes : 🤔\n\n⭕️ Not " \
               "released yet</code>\n⭕️ <a href='https://www.google.com/search?q={}'> Spelled incorrectly</a>\n" \
               "<code>⭕️ Unwanted texts in Msgs\n⭕ Asking theatre prints\n⭕ Not in ma Database</code>"
    BLOCK_LIST = ['http://', 'https://', '@', '#', 'bit.ly', 't.me', '/']
