import asyncio
import os
from telethon import TelegramClient, events, sync

api_id = 20581589
api_hash = 'ecbdbafc89f87c4d5e41b164cac7583d'
bot_token = '6038137070:AAF96LJG1FHrbRoNI8VBoYLWbveR9V31icQ'
channel_username = '@xlsxs'#телеграмм канал
folder_path = 'C:/Users/sk1/Documents/kakjaskd'#путь к папке которая будет мониторится кодом



client = TelegramClient('new_session', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage())
async def my_event_handler(event):
    pass

async def send_file_to_channel(file_path):

    await client.send_file(channel_username, file_path)


    #os.remove(file_path)убери комментарий если хочешь чтобы файл удалялся с пк после отправки

async def monitor_folder():
    sent_files_path = os.path.join(folder_path, 'sented_files.txt')
    sent_files = []

    if os.path.exists(sent_files_path):
        with open(sent_files_path, 'r') as file:
            sent_files = file.read().splitlines()

    while True:
        files = os.listdir(folder_path)
        xlsx_files = [f for f in files if f.endswith('.xlsx') and f not in sent_files]

        for file in xlsx_files:
            try:
                await send_file_to_channel(os.path.join(folder_path, file))
                sent_files.append(file)
            except Exception as e:
                print(f"Error sending file {file}: {e}")

        with open(sent_files_path, 'w') as file:
            file.write('\n'.join(sent_files))

        await asyncio.sleep(10)
with client:
    client.loop.create_task(monitor_folder())
    client.run_until_disconnected()