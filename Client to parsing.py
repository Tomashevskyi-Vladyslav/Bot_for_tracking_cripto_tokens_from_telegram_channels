from telethon import TelegramClient, events

# Replace these with your own values
api_id = 'your api id'
api_hash = 'your api hash'

client = TelegramClient('anon', api_id, api_hash)
client.start()

@client.on(events.NewMessage('channel from which views will come'))
async def main(event):
    global counter
    await client.send_message('bot that will receive notifications', event.message)
    print("+")

client.run_until_disconnected()  