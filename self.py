from telethon.sync import TelegramClient , events , Button
import time , requests , os , random , sys
from urllib.parse import urlparse
from telethon.tl.functions.messages import SendReactionRequest
import emoji
import asyncio , aiocron , pytz , time
from telethon.tl import functions
from datetime import datetime
from random import choice
#-------------------------------------------------------------------
api_id = 16365825
api_hash = 'becf667f7a469ef42103585c09dbc334'
with TelegramClient(sys.argv[1], api_id, api_hash) as client:
   client.send_message('me', "✅ با موفقیت سلف روی اکانت شما ران شد میتوانید با ارسال پیام\n`/help`\nکامند های ربات رو دریافت کنید با تشکر سازنده ربات آراز\n\n🆔 @ReaLAraz")
#   print(client.download_profile_photo('me'))
print("         Self Runned")
AdminBot = sys.argv[1] # آیدی عددی اکانتی که میخاید ران کنید
main = '9876543210'
fonts = ['９８７６５４３２１０']
heart = ['🖤','💜','💙','💚','💛','🧡','❤','🤍',]
name_list = []
bio_list = []
reaction = emoji.emojize(':red_heart:')
reaction = '❤️'
reaction = '\u2764'
admin = int(sys.argv[1])
STATUS = True
BOLD = False
WRITER = False
ITALIC = False
STRIKE = False
DENIED = ['/id', '/ping', '/time', '/mute', '/unmute', '/cleanmute', '/porn', '/ip <host>', '/on', '/off', '/italic on', '/bold on', '/writer on', '/strike on', '/italic off', '/bold off', '/writer off', '/strike off', '/spam1 <count> <Text>', '/spam2 <count> <Text>', '/shot1 <website>', '/shot2 <website>', '/fosh1 <count>', '/fosh2 <count> <username/id>', '/mydelete <count/max=4000>', '/delete <count/max=100>', '/enemy', '/delenemy']
mute_list = []
enemy_list = []

FOSH = open("fosh.txt",encoding="utf-8").readlines()
#-------------------------------------------------------------------
@client.on(events.NewMessage(pattern="/ping"))
async def Start(event):
    global admin , STATUS
    if event.sender_id == admin and STATUS == True:
        start = time.time()
        requests.get("https://google.com")
        ping = str(round( time.time() - start,4) )
        await event.edit(f"𝑷𝒊𝒏𝒈 **:** __{ping}__")

@client.on(events.NewMessage(pattern="/help"))
async def Start(event):
    global admin , STATUS
    if event.sender_id == admin and STATUS == True:
        t= """𝐔𝐬𝐞𝐫 𝐁𝐨𝐭 𝐇𝐞𝐥𝐩 :

- /id : get user id with reply or in pv
- /ping : real server ping 
- /time : Now Time
- /mute : Mute with reply or in pv
- /unmute : Unmute with reply or in pv
- /cleanmute : clean mute list
- /porn : Randomly Porn from database
- /ip <host> : full host info 
- /on : Turn user bot on
- /off : Trun user bot off
- /italic on : Turn italic mode on
- /bold on : Turn Bold mode on
- /writer on : Turn Writer mode on
- /strike on : Turn Strike mode on
- /italic off : Turn italic mode off
- /bold off : Turn Bold mode off
- /writer off : Turn Writer mode off
- /strike off : Turn Strike mode off
- /spam1 <count> <Text> : spam text in lines
- /spam2 <count> <Text> : spam text in one line 
- /shot1 <website> : screenshot from website ( compressed image )
- /shot2 <website> : screenshot from website ( not compressed image )
- /fosh1 <count> : kosnane taraf with reply
- /fosh2 <count> <username/id> : kosnane taraf with username
- /mydelete <count/max=4000> : delete own message 
- /delete <count/max=100> : delete chat message
- /enemy : enemy with reply or in pv
- /delenemy : delete enemy with reply or in pv
- /addname <name> : add time name
- /addbio <bio> : add time bio
- /delname <name> : delete time name
- /delbio <bio> : delete time bio
- /clearname : delete all name list
- /clearbio : delete all name list
- /timename on : online the name
- /timebio on : online the name 
- /timename off : offline the name
- /timebio off : offline the bio

𝐂𝐨𝐝𝐞𝐝 𝐁𝐲 : @ReaLAraz"""
        await event.edit(t)
@client.on(events.NewMessage(pattern="/id"))
async def Start(event):
    global admin , STATUS
    if event.sender_id == admin and STATUS == True:
        try:
            message = await event.get_reply_message()
            await event.edit("𝑰𝑫 **:** `"+str(message.from_id.user_id)+'`')
        except:
            chat = await event.get_chat()
            await event.edit("𝑰𝑫 **:** `"+str(chat.id)+'`')


@client.on(events.NewMessage(pattern="/off"))
async def Start(event):
    global admin , STATUS
    if event.sender_id == admin and STATUS == True:
        STATUS = False
        await event.edit("𝑼𝒔𝒆𝒓 𝒃𝒐𝒕 𝒕𝒖𝒓𝒏𝒆𝒅 𝒐𝒇𝒇.")

@client.on(events.NewMessage(pattern="/on"))
async def Start(event):
    global admin , STATUS
    if event.sender_id == admin and STATUS == False:
        STATUS = True
        await event.edit("𝑼𝒔𝒆𝒓 𝒃𝒐𝒕 𝒕𝒖𝒓𝒏𝒆𝒅 𝒐𝒏.")

@client.on(events.NewMessage(pattern="/spam1"))
async def Start(event):
    global admin , STATUS
    if event.sender_id == admin and STATUS == True:
        try:
            count = int(event.text.split(" ")[1])
        except:
            await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒏𝒖𝒎𝒃𝒆𝒓. /spam1 <count> <Text>")
        try:
            text = event.text.split("/spam1 "+str(count)+" ")[1]
            for i in range(count):
                await event.respond(text)
            await event.delete()
        except:
            await event.edit("𝑬𝒓𝒓𝒐𝒓 ,  𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒕𝒆𝒙𝒕. /spam1 <count> <Text>")

@client.on(events.NewMessage(pattern="/spam2"))
async def Start(event):
    global admin , STATUS
    if event.sender_id == admin and STATUS == True:
        text2 = ""
        try:
            count = int(event.text.split(" ")[1])
        except:
            await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒏𝒖𝒎𝒃𝒆𝒓. /spam2 <count> <Text>")
        try:
            text = event.text.split("/spam2 "+str(count)+" ")[1]
            for i in range(count):
                text2 += text+"\n"

            await event.respond(text2)
            await event.delete()
        except:
            await event.edit("𝑬𝒓𝒓𝒐𝒓 ,  𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒕𝒆𝒙𝒕. /spam2 <count> <Text>")

@client.on(events.NewMessage(pattern="/ip"))
async def Start(event):
    global admin , STATUS
    try:
        if event.sender_id == admin and STATUS == True:
            hostname = event.text.split(' ')[1]
            if "http" in hostname:
                hostname = urlparse(hostname).netloc

            response = requests.get('http://ip-api.com/json/'+hostname)
            response = response.json()
            status = response['status']
            country = response['country']
            regionName = response['regionName']
            city = response['city']
            isp = response['isp']
            ip = response['query']
            await event.edit('ᴅᴏᴍᴀɪɴ : **'+hostname.capitalize()+'**\nɪᴘ : **'+ip+'**\nᴄᴏᴜɴᴛʀʏ : **'+country+'**\nʀᴇɢɪᴏɴ : **'+regionName+'**\nᴄɪᴛʏ : **'+city+'**\nɪsᴘ : **'+isp+'**')
    except:
        await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒉𝒐𝒔𝒕. /ip <host>")
    
@client.on(events.NewMessage(pattern="/shot1"))
async def Start(event):
    global admin , STATUS
    try:
        if event.sender_id == admin and STATUS == True:
            try:
                url = event.text.split(" ")[1]
                a1 = await event.edit("𝑻𝒂𝒌𝒊𝒏𝒈 𝒔𝒄𝒓𝒆𝒆𝒏𝒔𝒉𝒐𝒕...")
            except:
                await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒘𝒆𝒃𝒔𝒊𝒕𝒆. /shot2 <website>")
            r1 = requests.get("http://mini.site-shot.com/x/codebazan.ir-Web-screenshot/1000/png/?"+url,timeout=6)
            open("cap.jpg",'wb').write(r1.content)
            await a1.delete()
            await event.respond(f"𝑺𝒄𝒓𝒆𝒆𝒏𝒔𝒉𝒐𝒕 𝒇𝒓𝒐𝒎 [link]({url}).\n\n𝑷𝒐𝒘𝒆𝒓𝒆𝒅 𝒃𝒚 : `@UranusSelf`",file="cap.jpg")
            
            os.remove("cap.jpg")
    except:
        await event.edit("𝑼𝒏𝒆𝒙𝒑𝒆𝒄𝒕𝒆𝒅 𝒆𝒓𝒓𝒐𝒓.")

@client.on(events.NewMessage(pattern="/shot2"))
async def Start(event):
    global admin , STATUS
    try:
        if event.sender_id == admin and STATUS == True:
            try:
                url = event.text.split(" ")[1]
                a1 = await event.edit("𝑻𝒂𝒌𝒊𝒏𝒈 𝒔𝒄𝒓𝒆𝒆𝒏𝒔𝒉𝒐𝒕...")
            except:
                await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒘𝒆𝒃𝒔𝒊𝒕𝒆. /shot2 <website>")
            r1 = requests.get("http://mini.site-shot.com/x/codebazan.ir-Web-screenshot/1000/png/?"+url,timeout=6)
            open("cap.jpg",'wb').write(r1.content)
            await a1.delete()
            await event.respond(f"𝑺𝒄𝒓𝒆𝒆𝒏𝒔𝒉𝒐𝒕 𝒇𝒓𝒐𝒎 [link]({url}).\n\n𝑷𝒐𝒘𝒆𝒓𝒆𝒅 𝒃𝒚 : `@UranusSelf`",file="cap.jpg",force_document=True)
            
            os.remove("cap.jpg")
    except:
        await event.edit("𝑼𝒏𝒆𝒙𝒑𝒆𝒄𝒕𝒆𝒅 𝒆𝒓𝒓𝒐𝒓.")

@client.on(events.NewMessage(pattern="/fosh1",func=lambda e:e.is_reply))
async def Start(event):
    global admin , STATUS , FOSH
    if event.sender_id == admin and STATUS == True:
        try:
            chat = await event.get_chat()
            message = await event.get_reply_message()
            count = int(event.text.split("/fosh1 ")[1])
            await event.delete()
            for i in range(count):
                await client.send_message(chat.id,random.choice(FOSH),reply_to=message.id)
        except:
            await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒏𝒖𝒎𝒃𝒆𝒓. /fosh1 <count>")
            
@client.on(events.NewMessage(pattern="/fosh2"))
async def Start(event):
    global admin , STATUS , FOSH
    if event.sender_id == admin and STATUS == True:
            try:
                count = int(event.text.split(" ")[1])
            except:
                await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒏𝒖𝒎𝒃𝒆𝒓. /fosh2 <count> <username/id>")
                requests.get("asds")
            try:
                text = event.text.split("/fosh2 "+str(count)+" ")[1]
            except:
                await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝑼𝒔𝒆𝒓. /fosh2 <count> <username/id>")
                requests.get("asds")
            await event.delete()
            if "@" in text:
                for i in range(count):
                    await event.respond(random.choice(FOSH)+"\n"+text)
            elif text.isnumeric():
                for i in range(count):
                    await event.respond(random.choice(FOSH)+"\n[kosnanat](tg://user?id="+text+")")
            else:
                await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝑼𝒔𝒆𝒓. /fosh2 <count> <username/id>")
            
@client.on(events.NewMessage(pattern="/fosh2"))
async def Start(event):
    global admin , STATUS , FOSH
    if event.sender_id == admin and STATUS == True:
            try:
                count = int(event.text.split(" ")[1])
            except:
                await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒏𝒖𝒎𝒃𝒆𝒓. /fosh2 <count> <username/id>")
                requests.get("asds")
            try:
                text = event.text.split("/fosh2 "+str(count)+" ")[1]
            except:
                await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝑼𝒔𝒆𝒓. /fosh2 <count> <username/id>")
                requests.get("asds")
            await event.delete()
            if "@" in text:
                for i in range(count):
                    await event.respond(random.choice(FOSH)+"\n"+text)
            elif text.isnumeric():
                for i in range(count):
                    await event.respond(random.choice(FOSH)+"\n[kosnanat](tg://user?id="+text+")")
            else:
                await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝑼𝒔𝒆𝒓. /fosh2 <count> <username/id>")

@client.on(events.NewMessage(pattern="/porn"))
async def Start(event):
    global admin , STATUS 
    if event.sender_id == admin and STATUS == True:
        messages=await client.get_messages("selfp0rno",limit=int(200))
        mm = random.choice(messages)
        timee1 = str(round(mm.document.attributes[0].duration / 60,2)).split(".")[0]
        timee2 = str(round(mm.document.attributes[0].duration / 60,2)).split(".")[1]
        if len(list(timee1)) != 2:
            timee1 = "0"+timee1
        elif len(list(timee2)) != 2:
            timee2 = "0"+timee2

        mm.text = "𝒀𝒐𝒖𝒓 𝒑𝒐𝒓𝒏 𝒓𝒆𝒒𝒖𝒆𝒔𝒕 𝒓𝒆𝒔𝒖𝒍𝒕.\n\n𝑽𝒊𝒅𝒆𝒐 𝑽𝒐𝒍𝒖𝒎𝒆 : "+str(round(mm.document.size / 1000000,2))+" MB\n"+"𝑫𝒖𝒓𝒂𝒕𝒊𝒐𝒏 : "+timee1+":"+timee2+" min"+"\n\n𝑷𝒐𝒘𝒆𝒓𝒆𝒅 𝒃𝒚 : `@UranusSelf`"
        await event.respond(mm)

@client.on(events.NewMessage(pattern="/mydelete"))
async def Start(event):
    global admin , STATUS
    if event.sender_id == admin and STATUS == True:
        try:
            group = await event.get_chat()
            group = int("-100" + str(group.id))
            count = event.text.split(" ")[1]
            if int(count) <= 4000:
            
                messages=await client.get_messages(group,limit=int(count))
                for a in messages:
                    try:
                        if a.from_id.user_id == admin:
                            await client.delete_messages(group,a.id)

                    except:
                        pass
            else:
                await event.edit("𝒀𝒐𝒖 𝑪𝒂𝒏'𝒕 𝒅𝒆𝒍𝒆𝒕𝒆 𝒎𝒐𝒓𝒆 𝒕𝒉𝒂𝒏 4000.")
        except:
            await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒏𝒖𝒎𝒃𝒆𝒓. /mydelete <count>")

@client.on(events.NewMessage(pattern="/mute"))
async def Start(event):
    global admin , STATUS , mute_list
    if event.sender_id == admin and STATUS == True:
        try:
            message = await event.get_reply_message()
            mute_list.append(message.from_id.user_id)
            await event.edit("𝑴𝒖𝒕𝒆𝒅.")
        except:
            chat = await event.get_chat()
            mute_list.append(chat.id)
            await event.edit("𝑴𝒖𝒕𝒆𝒅.")

@client.on(events.NewMessage(pattern="/unmute"))
async def Start(event):
    global admin , STATUS , mute_list
    if event.sender_id == admin and STATUS == True:
        try:
            message = await event.get_reply_message()
            mute_list.remove(message.from_id.user_id)
            await event.edit('𝑼𝒏𝒎𝒖𝒕𝒆𝒅.')
        except:
            chat = await event.get_chat()
            mute_list.remove(chat.id)
            await event.edit("𝑼𝒏𝒎𝒖𝒕𝒆𝒅.")

@client.on(events.NewMessage(pattern="/cleanmute"))
async def Start(event):
    global admin , STATUS , mute_list
    if event.sender_id == admin and STATUS == True:
        mute_list = []
        await event.edit("𝑴𝒖𝒕𝒆 𝑳𝒊𝒔𝒕 𝑪𝒍𝒆𝒂𝒏𝒆𝒅.")

@client.on(events.NewMessage(pattern="/time"))
async def Start(event):
    global admin , STATUS , mute_list
    if event.sender_id == admin and STATUS == True:
        try:
            r = requests.get("http://api.codebazan.ir/time-date/?json=all",timeout=5).json()
            t = f"""{r['result']['dateen']} ~ {r['result']['timeen']}
{r['result']['datefa']} ~ {r['result']['timefa']}

𝑷𝒐𝒘𝒆𝒓𝒆𝒅 𝒃𝒚 : `@UranusSelf`"""
            await event.edit(t)
        except:
            await event.edit("𝑼𝒏𝒆𝒙𝒑𝒆𝒄𝒕𝒆𝒅 𝒆𝒓𝒓𝒐𝒓.")

@client.on(events.NewMessage(pattern="/delete"))
async def Start(event):
    global admin , STATUS
    if event.sender_id == admin and STATUS == True:  
        try:
            chat = await event.get_chat()
            mes = int(event.text.split("/delete ")[1])
            now = event.id + 1
            end = now - mes
            await client.delete_messages(chat.id,[i for i in range(end,now)])  
        except:
            await event.edit("𝑬𝒓𝒓𝒐𝒓 , 𝒆𝒏𝒕𝒆𝒓 𝒄𝒐𝒓𝒓𝒆𝒄𝒕 𝒏𝒖𝒎𝒃𝒆𝒓. /delete <count>")

@client.on(events.NewMessage(pattern="/enemy"))
async def Start(event):
    global admin , STATUS , enemy_list
    if event.sender_id == admin and STATUS == True:  
        try:
            message = await event.get_reply_message()
            enemy_list.append(message.from_id.user_id)
            await event.edit('𝑨𝒅𝒅𝒆𝒅 𝑻𝒐 𝑬𝒏𝒆𝒎𝒚.')
        except:
            chat = await event.get_chat()
            enemy_list.append(chat.id)
            await event.edit("𝑨𝒅𝒅𝒆𝒅 𝑻𝒐 𝑬𝒏𝒆𝒎𝒚.")

@client.on(events.NewMessage(pattern="/delenemy"))
async def Start(event):
    global admin , STATUS , enemy_list
    if event.sender_id == admin and STATUS == True:  
        try:
            message = await event.get_reply_message()
            enemy_list.remove(message.from_id.user_id)
            await event.edit('𝑹𝒆𝒎𝒐𝒗𝒆𝒅 𝒇𝒓𝒐𝒎 𝑬𝒏𝒆𝒎𝒚.')
        except:
            chat = await event.get_chat()
            enemy_list.remove(chat.id)
            await event.edit("𝑹𝒆𝒎𝒐𝒗𝒆𝒅 𝒇𝒓𝒐𝒎 𝑬𝒏𝒆𝒎𝒚.")

@client.on(events.NewMessage())
async def Bold(event):
    global admin , STATUS , BOLD , WRITER , ITALIC , STRIKE , mute_list , enemy_list , FOSH , DENIED
    if event.sender_id == admin and STATUS == True and event.text.lower() == "/bold on":
        BOLD = True
        await event.edit("𝑩𝒐𝒍𝒅 𝑻𝒖𝒓𝒏𝒆𝒅 𝑶𝒏.")
    elif event.sender_id == admin and STATUS == True and event.text.lower() == "/bold off" and event.text not in DENIED:
        BOLD = False
        await event.edit("𝑩𝒐𝒍𝒅 𝑻𝒖𝒓𝒏𝒆𝒅 𝑶𝒇𝒇.")
    elif event.sender_id == admin and STATUS == True and event.text.lower() == "/writer on" and event.text not in DENIED:
        WRITER = True
        await event.edit("𝑾𝒓𝒊𝒕𝒆𝒓 𝑻𝒖𝒓𝒏𝒆𝒅 𝑶𝒏.")
    elif event.sender_id == admin and STATUS == True and event.text.lower() == "/writer off" and event.text not in DENIED:
        WRITER = False
        await event.edit("𝑾𝒓𝒊𝒕𝒆𝒓 𝑻𝒖𝒓𝒏𝒆𝒅 𝑶𝒇𝒇.")
    elif event.sender_id == admin and STATUS == True and event.text.lower() == "/italic on" and event.text not in DENIED:
        ITALIC = True
        await event.edit("𝑰𝒕𝒂𝒍𝒊𝒄 𝑻𝒖𝒓𝒏𝒆𝒅 𝑶𝒏.")
    elif event.sender_id == admin and STATUS == True and event.text.lower() == "/italic off" and event.text not in DENIED:
        ITALIC = False
        await event.edit("𝑰𝒕𝒂𝒍𝒊𝒄 𝑻𝒖𝒓𝒏𝒆𝒅 𝑶𝒇𝒇.")
    elif event.sender_id == admin and STATUS == True and event.text.lower() == "/strike on" and event.text not in DENIED:
        STRIKE = True
        await event.edit("𝑺𝒕𝒓𝒊𝒌𝒆 𝑻𝒖𝒓𝒏𝒆𝒅 𝑶𝒏.")
    elif event.sender_id == admin and STATUS == True and event.text.lower() == "/strike off" and event.text not in DENIED:
        STRIKE = False
        await event.edit("𝑺𝒕𝒓𝒊𝒌𝒆 𝑻𝒖𝒓𝒏𝒆𝒅 𝑶𝒇𝒇.")
    elif event.sender_id == admin and STATUS == True and BOLD == True:
        await event.edit("**"+event.text+"**")
    elif event.sender_id == admin and STATUS == True and WRITER == True:
        await event.edit("`"+event.text+"`")
    elif event.sender_id == admin and STATUS == True and ITALIC == True:
        await event.edit("__"+event.text+"__")
    elif event.sender_id == admin and STATUS == True and STRIKE == True:
        await event.edit("~~"+event.text+"~~")
    elif event.sender_id in mute_list:
        await event.delete()
    elif event.sender_id in enemy_list:
        await event.reply(random.choice(FOSH))
        
@client.on(events.NewMessage(pattern=r"/addname (.*)" , from_users=AdminBot))
async def add_name(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    xxx = (input_str)
    if (xxx) in name_list:
        await event.edit(f"**Name ( {xxx} ) In Name Listed . . . !**")
    else:
        try:
            name_list.append(xxx)
            await event.edit(f"**Name ( {xxx} ) Aded In List Name . . . !**")
        except:
            await event.edit("**No Invalid . . . !**")

@client.on(events.NewMessage(pattern=r"/delname (.*)" , from_users=AdminBot))
async def del_name(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    xxx = (input_str)
    if (xxx) not in name_list:
        await event.edit(f"**Name ( {xxx} ) Not In Name Listed . . . !**")
    else:
        try:
            name_list.remove(xxx)
            await event.edit(f"**Name ( {xxx} ) Removed In List Name . . . !**")
        except:
            await event.edit("**No Invalid . . . !**")

@client.on(events.NewMessage())
async def clean_name(event):
    text = (event.raw_text)
    if (text == "/clearname" and event.sender_id == AdminBot):
        if name_list == []:
            await event.edit("**Name List Has Been Empty . . . !**")
        else:
            name_list.clear()
            await event.edit("**Name List Has Been Cleared . . . !**")

@client.on(events.NewMessage(pattern=r"/addbio (.*)" , from_users=AdminBot))
async def add_bio(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    xxx = (input_str)
    if (xxx) in bio_list:
        await event.edit(f"**Bio ( {xxx} ) In Bio Listed . . . !**")
    else:
        try:
            bio_list.append(xxx)
            await event.edit(f"**Bio ( {xxx} ) Aded In List Bio . . . !**")
        except:
            await event.edit("**No Invalid . . . !**")

@client.on(events.NewMessage(pattern=r"/delbio (.*)" , from_users=AdminBot))
async def del_bio(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    xxx = (input_str)
    if (xxx) not in bio_list:
        await event.edit(f"**Bio ( {xxx} ) Not In Bio Listed . . . !**")
    else:
        try:
            bio_list.remove(xxx)
            await event.edit(f"**Bio ( {xxx} ) Removed In List Bio . . . !**")
        except:
            await event.edit("**No Invalid . . . !**")

@client.on(events.NewMessage())
async def clean_bio(event):
    text = (event.raw_text)
    if (text == "/clearbio" and event.sender_id == AdminBot):
        if bio_list == []:
            await event.edit("**Bio List Has Been Empty . . . !**")
        else:
            bio_list.clear()
            await event.edit("**Bio List Has Been Cleared . . . !**")

@client.on(events.NewMessage())
async def timebio_on(event):
    text = (event.raw_text)
    if (text == "/timebio on" and event.sender_id == AdminBot):
        if bio_list == []:
            await event.edit("**You Must First Have A Name In The List Of Names . . . !**")
        else:
            await event.edit(f'**Time Bio Is [Actived](tg://user?id={AdminBot}) !**')
            @aiocron.crontab('*/1 * * * *')
            async def clockbio():
                ir=pytz.timezone("Asia/Tehran")
                time=datetime.now(ir).strftime("%H:%M")
                time=time.translate(time.maketrans(main, choice(fonts)))
                await client(functions.account.UpdateProfileRequest(about=f'{choice(heart)} {choice(bio_list)} {time}'))
                clockbio.start()

@client.on(events.NewMessage())
async def timename_on(event):
    text = (event.raw_text)
    if (text == "/timename on" and event.sender_id == AdminBot):
        if name_list == []:
            await event.edit("**You Must First Have A Name In The List Of Names . . . !**")
        else:
            await event.edit(f'**Time Name Is [Actived](tg://user?id={AdminBot}) !**')
            @aiocron.crontab('*/1 * * * *')
            async def clockname():
                ir=pytz.timezone("Asia/Tehran")
                time=datetime.now(ir).strftime("%H:%M")
                time=time.translate(time.maketrans(main, choice(fonts)))
                await client(functions.account.UpdateProfileRequest(first_name=f'{choice(name_list)} {choice(heart)} {time}'))
                clockname.start()

@client.on(events.NewMessage())
async def timename_off(event):
    text = (event.raw_text)
    if (text == "/timename on" and event.sender_id == AdminBot):
        await event.edit(f'**Time Name Is [DeActived](tg://user?id={AdminBot}) !**')
        clockname.stop()

@client.on(events.NewMessage())
async def timebio_off(event):
    text = (event.raw_text)
    if (text == "/timebio off" and event.sender_id == AdminBot):
        await event.edit(f'**Time Bio Is [DeActived](tg://user?id={AdminBot}) !**')
        clockbio.stop()
client.start()
client.run_until_disconnected()
asyncio.get_event_loop().run_forever()
