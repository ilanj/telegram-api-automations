import time

from telethon import *
from telethon.errors import FloodWaitError

from telethon.client import client
from datetime import datetime
now = datetime.now()
print(now)
# print(client.get_me().stringify())
for no in range(0,15000):
    try:
        now = datetime.now()
        print(str(no)+"---->"+str(now))
        client.send_message('mob_no', str(no)+"---->"+str(now))
    except FloodWaitError:
        print("waiting at eception")
        time.sleep(305)
# client.send_file('+mob_no', 'fefef.jpg')

# client.download_profile_photo('+mob_no')
# messages = client.get_messages('+mob_no')
# messages[0].download_media()

@client.on(events.NewMessage(pattern='(?i)hi|hello'))
async def handler(event):
    await event.respond('Hey!')