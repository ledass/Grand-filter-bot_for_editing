# Bot information
SESSION = 'Media_search'
USER_SESSION = 'User_Bot'
API_ID = 12345
API_HASH = '0123456789abcdef0123456789abcdef'
BOT_TOKEN = '123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11'
USERBOT_STRING_SESSION = ''

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = False

# Admins, Channels & Users
ADMINS = [12345789, 'admin123', 98765432]
CHANNELS = [-10012345678, -100987654321, 'channelusername']
AUTH_USERS = []
AUTH_CHANNEL = None

# MongoDB information
DATABASE_URI = "mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb]?retryWrites=true&w=majority"
DATABASE_NAME = 'Telegram'
COLLECTION_NAME = 'channel_files'  # If you are using the same database, then use different collection name for each bot

HELPMSG = """
**You can find the bot commands here.**
**User Commands:-**
/help - Show this help message
/settings - Toggle settings of Precise 

Admin Commands:-
/logs - Get logs as a file
/group_broadcast  - to broadcast a message to all groups
/stats - Get bot user stats
/broadcast - Reply to a message to send that to all bot users
/index - Start indexing a database channel (bot must be admin of the channel if that is provate channel)
You can just forward the message from database channel for starting indexing, no need to use the /index 
/ban - Ban a user from bot - /ban user_id
/unban - Unban a user from bot - /unban user_id
/filter - add manual filters 
/filters - view filters
/delall - delete all filters    
id - get tg ids 
/imdb - fetch info from imdb
/alive - check bot alive  
/ping - pong  
/gfilter - to add a global filter 
/delg - to delete a global filter
"""

STARTMSG = """<b>𝖧𝖾𝗅𝗅𝗈.... {} 💖

I am a an autofilter bot which finds & shares media from my database.</b>"""
