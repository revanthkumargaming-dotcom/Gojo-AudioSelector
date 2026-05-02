# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 Gojo
# 𝐓𝐆 𝐈𝐃 : @SATORO_GOJO_limitless
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --

import os

# Telegram API credentials
API_ID =   "35915041"
API_HASH = "011fabdce4a5547ce2e56533862445ad"  
BOT_TOKEN = "8676962323:AAFinOsrTP_RXBRcT8ycq6bOJYiMVqyRidM"  

# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 Gojo
# 𝐓𝐆 𝐈𝐃 : @SATORO_GOJO_limitless
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --

# Directory for downloads
DOWNLOAD_DIR = "downloads"

# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 Gojo
# 𝐓𝐆 𝐈𝐃 : @SATORO_GOJO_limitless
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --

# Allowed group IDs
ALLOWED_GROUP_IDS = [-1003857287675
    ,  # Your group ID from logs
    # Add more group IDs as needed
]

# Owner user ID
OWNER_ID =   "6334669810"

# Maximum file size (e.g., 4GB)
MAX_FILE_SIZE = 4 * 1024 * 1024 * 1024  # 4GB in bytes

# Premium users and daily limits
PREMIUM_USERS = {7340960697}  # Add premium user IDs here
DAILY_LIMIT_FREE = 15  # Videos per day for free users
DAILY_LIMIT_PREMIUM = 30  # Videos per day for premium users

# Ensure download directory exists
os.makedirs(DOWNLOAD_DIR, exist_ok=True)
if not os.access(DOWNLOAD_DIR, os.W_OK):
    raise PermissionError(f"No write permission for {DOWNLOAD_DIR}")
# ----------------------------------------
# 𝐌𝐀𝐃𝐄 𝐁𝐘 Gojo
# 𝐓𝐆 𝐈𝐃 : @SATORO_GOJO_limitless
# 𝐀𝐍𝐘 𝐈𝐒𝐒𝐔𝐄𝐒 𝐎𝐑 𝐀𝐃𝐃𝐈𝐍𝐆 𝐌𝐎𝐑𝐄 𝐓𝐇𝐈𝐍𝐆𝐬 𝐂𝐀𝐍 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄
# --
