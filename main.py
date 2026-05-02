# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 Gojo
# 𝐓𝐆 𝐈𝐃 : @SATORO_GOJO_limitless
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
import os
from flask import Flask
from threading import Thread
from pyrogram import Client

web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "Alive"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web_app.run(host="0.0.0.0", port=port, threaded=True)

Thread(target=run_web, daemon=True).start()

bot = Client(
    "bot",
    api_id=int(os.environ["35915041"]),
    api_hash=os.environ["011fabdce4a5547ce2e56533862445ad"],
    bot_token=os.environ["8676962323:AAFinOsrTP_RXBRcT8ycq6bOJYiMVqyRidM"]
)

print("Bot Starting...")
bot.run()
import os
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
import logging
from start import register_start_handlers
from status import register_status_handlers
from us import register_us_handlers
from video import register_video_handlers
from cancel import register_cancel_handlers
from getid import register_getid_handlers
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 Gojo
# 𝐓𝐆 𝐈𝐃 : @SATORO_GOJO_limitless
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Pyrogram client
app = Client("audio_selector_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐀𝐁𝐇𝐈
# 𝐓𝐆 𝐈𝐃 : @𝐂𝐋𝐔𝐓𝐂𝐇𝟎𝟎𝟖
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
def main():
    """Main function to start the bot."""
    register_start_handlers(app)
    register_status_handlers(app)
    register_us_handlers(app)
    register_video_handlers(app)
    register_cancel_handlers(app)
    register_getid_handlers(app)
    logger.info("Starting bot...")
    app.run()

if __name__ == "__main__":
    main()
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 Gojo
# 𝐓𝐆 𝐈𝐃 : @SATORO_GOJO_limitless
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# ----------------------------------------
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot Running"

app.run(host="0.0.0.0", port=10000)
