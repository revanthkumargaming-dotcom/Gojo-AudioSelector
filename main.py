import os
import logging
from flask import Flask
from threading import Thread
from pyrogram import Client

from config import API_ID, API_HASH, BOT_TOKEN
from start import register_start_handlers
from status import register_status_handlers
from us import register_us_handlers
from video import register_video_handlers
from cancel import register_cancel_handlers
from getid import register_getid_handlers

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Flask keep alive
web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "Bot Running"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    web_app.run(host="0.0.0.0", port=port, threaded=True)

Thread(target=run_web, daemon=True).start()

# Telegram Bot
app = Client(
    "audio_selector_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

def main():
    register_start_handlers(app)
    register_status_handlers(app)
    register_us_handlers(app)
    register_video_handlers(app)
    register_cancel_handlers(app)
    register_getid_handlers(app)

    logger.info("Bot Starting...")
    app.run()

if __name__ == "__main__":
    main()
