from telethon import TelegramClient, events
import modullar.client
client = modullar.client.client

@events.register(events.NewMessage(pattern=".hjelp"))
async def help(event):
	await event.edit("""
ð  **Umumiy modullar**: 16
â **Berkitilgan modullar**:  3

ð **Tezlik**: ping.
ð **Birdaniga hammani ban qilish**: banall.
ð **Spamm habar**: spam. <soniya> <takrorlanish> <habar>
ð **Textni emojiga aylantiradi**: emoji. <Text>
ð **Guruh malumotlarini scanerlaydi**: chatinfo.
ð **Chatlaringiz sonini hisoblaydi**: count.
ð **Base64 da shifrlaydi**: b64. <en> <reply>
ð **Base64 shifrdan yechadi**: b64. <de> <reply>
ð **Memli sticker**: mq. <reply>
ð **Text sticker**: qq. <reply>
ð **Text image**: nq. <reply>
ð **Qr code yaratadi**: qrc. <create> <reply>
ð **Textni teskari ogiradi**: rev. <reply>
ð **Guruh azolarini chaqiradi**: tagall. 
ð **Nickname ozgartiradi**: rename. <Nickname>
ð **Wiki qidiruv**: wiki. <qidirish uchun soÊ»z>

ð  ~~JOJO USERBOT~~ : @JOJO_USERBOT


""")