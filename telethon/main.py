from telethon import TelegramClient, events
from datetime import datetime

# Your API credentials (replace with your own values)
api_id = 123456
api_hash = 'xxx'
phone = '+91xxx'

# Create the client and connect
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    now = datetime.now()
    no = '+91xxx'  # Replace with the actual phone number or username you want to send the message to
    await client.send_message(no, str(no) + "---->" + str(now))


async def group_msg():
    group_username = 't.me/myapigroup'  # Example: 't.me/yourgroup' or -1001234567890
    message = "Hello, Group! This is a test message."

    # Send message to the group
    await client.send_message(group_username, message)
    print("Message sent successfully!")


@client.on(events.NewMessage(pattern='(?i)hi|hello'))
async def handler(event):
    await event.respond('Hey!')

group_msg()

with client:
    client.loop.run_until_complete(main())
    client.loop.run_until_complete(group_msg())
    # client.run_until_disconnected()

