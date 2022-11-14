from telethon import TelegramClient, events
import modullar.client
import os
import time
client = modullar.client.client

@events.register(events.NewMessage(outgoing=True, pattern='\.alive'))
async def alive(noob_py):
		client = noob_py.client
		me = await client.get_me()
		username = me.username
		anon1maus_xakker = await client.download_profile_photo(username)
		await client.edit_message(noob_py.message, "Hayrli kun...")
		time.sleep(0.5)
		await noob_py.respond("""🥷 **Foydalanuvchi**: @{}

🥷 **Versia**: 1.0.1.3
├╴╴╴╴╴╴╴╴╴╴
└ 🧟‍♀️ **DDMX Userbot**: @DDMX_userbot

 👾 **2021yil 10oy 19kun dasturlangan**
 👾 **ajdodi**: magicbot-uz
 👾 **Dasturchi**: @anon1maus_xakker

🥷 OʻRNATISH 
├╴╴╴╴╴╴╴╴╴╴
├ 👾 https://telegra.ph/DDMX--USERBOT---ORNATISH-BOYICHA-QO%CA%BBLLANMA-11-14
└ 👾 https://telegra.ph/DDMX--USERBOT---ORNATISH-BOYICHA-QO%CA%BBLLANMA-11-14""".format(username, ' '), file=anon1maus_xakker)
		await noob_py.message.delete()
		os.remove(anon1maus_xakker)