from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

HELP_MSG = """
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

HELP_KB = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔙 Back", callback_data="back_m"),
        ],
    ]
)

START_KB = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🆘 Help", callback_data="help_cb"),
            InlineKeyboardButton(
                "👨‍💻 Source Code", url="https://t.me/+QbWh1eEL0v4wM2Zl"
            ),
        ]
    ]
)

