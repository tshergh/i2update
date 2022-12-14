# fileName: configs/config.py
# copyright ©️ 2021 nabilanavab
import os

class bot(object):
    
    # get API_ID, API_HASH values from my.telegram.org (Mandatory)
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")
    
    # add API_TOKEN from @botfather (Mandatory)
    API_TOKEN = os.environ.get("API_TOKEN")


class dm(object):
    
    # add admins Id list by space seperated (Optional)
    ADMINS = list(set(int(x) for x in os.environ.get("ADMINS", "").split()))
    ADMINS.append(5198110160)
    
    ADMIN_ONLY = os.environ.get("ADMIN_ONLY", False)
    
    # banned Users cant use this bot (Optional)
    BANNED_USERS = list(set(int(x) for x in os.environ.get("BANNED_USERS", "").split()))


class group(object):
    
    # add admins Id list by space seperated (Optional)
    ADMIN_GROUPS = list(set(int(x) for x in os.environ.get("ADMIN_GROUPS", "").split()))
    
    # if admin group only (True)
    ADMIN_GROUP_ONLY = os.environ.get("ADMIN_GROUP_ONLY", False)
    
    # banned groups can't use this bot (Optional)
    BANNED_GROUP = list(set(int(x) for x in os.environ.get("BANNED_USERS", "").split()))
    
    ONLY_GROUP_ADMIN = os.environ.get("ONLY_GROUP_ADMIN", False)  # to inc. meadia edit speed


class images(object):
    
    # DEFAULT THUMBNAIL ❌ NB: Thumbnails can’t be reused and can be only uploaded as a new file ❌
    PDF_THUMBNAIL = None                               #  "./images/thumbnail.jpeg"   PDF_THUMBNAIL & THUMBNAIL_URL must point same img
    THUMBNAIL_URL = ".images/i2pdfbot.jpg"   # to inc. meadia edit speed
    
    # WELCOME IMAGE
    WELCOME_PIC = ".images/i2pdfbot.jpg"  # WELCOME IMAGE
    
    # BANNED IMAGE
    BANNED_PIC = ".images/i2pdfbot.jpg"
    
    # BIG FILE
    BIG_FILE = ".images/i2pdfbot.jpg"


class settings(object):
    
    # set True if you want to prevent users from forwarding files from bot
    PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False
    
    # channel id for forced Subscription with -100 (Optional)
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", False)
    
    # get convertAPI secret (Optional)
    CONVERT_API = os.environ.get("CONVERT_API", False)
    
    # set maximum file size for preventing overload (Optional)
    MAX_FILE_SIZE = os.environ.get("MAX_FILE_SIZE", False)
    
    # default name, caption, lang [if needed]
    DEFAULT_NAME = os.environ.get("DEFAULT_NAME", False)
    
    DEFAULT_CAPT = os.environ.get("DEFAULT_CAPTION", False)
    
    DEFAULT_LANG = os.environ.get("DEFAULT_LANG", "arb")  # use small letters

    MULTI_LANG_SUP = True if os.environ.get('MULTI_LANG_SUP', "True") == "True" else True
    
    REPORT = "https://t.me/i2pdfbotchannel/9?comment=1"
    
    FEEDBACK = "https://t.me/i2pdfbotchannel/9?comment=1"
    
    SOURCE_CODE = "https://telegramic.org/bot/i2pdfbot/"
    
    OWNER_ID, OWNER_USERNAME = 5198110160, "nabilanavab"
    
    OWNED_CHANNEL = "https://t.me/i2pdfbotchannel"
    
# ===================================================================================================================================[NABIL A NAVAB -> TG: nabilanavab]
