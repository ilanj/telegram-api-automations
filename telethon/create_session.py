from telethon import TelegramClient, events, sync

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 123456
api_hash = ''

client = TelegramClient('session_name', api_id, api_hash)
client.start()