import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "23898744")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "0b13c810c80b548604650cbe3c3db0c3") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7900603425:AAExRjcURz_m0jwA_AwP4WkXcq0NnziQC_8") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', 'Era_Bot_Support') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://filmyrohesh51:19SmDYqC1N5DqLkD@cluster0.jogzc68.mongodb.net/?retryWrites=true&w=majority")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","SnowEncoderBot") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "8108281129")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002381050327')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/af22bcdafa496d1f0c04c-d2bb1b5fbe230b18ac.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "1980"))


    caption = """
────────────────────────────
**ғɪʟᴇ ɴᴀᴍᴇ**: {0}

**ᴏʀɪɢɪɴᴀʟ ғɪʟᴇ sɪᴢᴇ:** {1}
**ᴇɴᴄᴏᴅᴇᴅ ғɪʟᴇ sɪᴢᴇ:** {2}
**ᴄᴏᴍᴘʀᴇssɪᴏɴ ᴘᴇʀᴄᴇɴᴛᴀɢᴇ:** {3}
────────────────────────────
__ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴ{4}__
__ ᴠɪᴅᴇᴏ ᴇɴᴄᴏᴅᴇᴅ ɪɴ{5}__
__ᴠɪᴅᴇᴏ ᴜᴘʟᴏᴀᴅᴇ ɪɴ{6}__
────────────────────────────
"""
