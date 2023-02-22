import telethon , os , requests
from telethon import TelegramClient , events , Button
ADMINS = [89733682]
BLACK_LIST = []
api_id = 16365825
api_hash = 'becf667f7a469ef42103585c09dbc334'
client = TelegramClient("basesaz", api_id, api_hash).start(bot_token="5748289963:AAHKDtFS7pwslaBWtsTC-hCIhaFWmkcdvI8")
fullinfo = {}
def check_join(ids):
    try:
        r = requests.get(f"https://api.telegram.org/bot5748289963:AAHKDtFS7pwslaBWtsTC-hCIhaFWmkcdvI8/getChatMember?chat_id=-1001394300011&user_id={str(ids)}").json()
        if str(r["result"]["status"]) != "member" and str(r["result"]["status"]) != "creator" and str(r["result"]["status"]) != "administrator":
            return False
        else:
            return  True
        
    except:
        return False


@client.on(events.NewMessage(pattern="/start",func=lambda e:e.is_private))
async def Start(event):
    global fullinfo
    fullinfo[event.sender_id]= {}
    sss = check_join(event.sender_id)
    if sss == True:
        ccc = open("data.txt").read().split("\n")
        if str(event.sender_id) not in ccc:
            try:
                os.remove(str(event.sender_id)+".session")
            except:
                pass
        
        await event.reply("🔰به ربات سلف ساز خوش آمدید. برای ادامه بر روی [ `☎️ ارسال شماره` ] کلیک کنید و شماره اکانت خود را به اشتراک بگذارید تا سلف نصب شود.",buttons=[[Button.request_phone("☎️ ارسال شماره",resize=1)]])
    else:
        await event.respond("""⁉️ برای استفاده از ربات ، در چنل زیر جوین شوید .

🌀 @UranusSelf

/start""")



@client.on(events.NewMessage(pattern="/code",func=lambda e:e.is_private))
async def Start(event):
    global fullinfo
    sss = check_join(event.sender_id)
    if sss == True:
        try:
            me = await fullinfo[event.sender_id]["client"].sign_in(fullinfo[event.sender_id]["phone"], code=event.text.split("/code ")[1].replace("-","").replace("۱","1").replace("۲","2").replace("۳","3").replace("۴","4").replace("۰","0").replace("۵","5").replace("۶","6").replace("۷","7").replace("۸","8").replace("۹","9"))
            await fullinfo[event.sender_id]["client"].disconnect()
#            os.system("screen -dm -S "+str(event.sender_id)+" python3 Non_Petros.py "+str(event.sender_id)+" "+str(me.id)+" "+str(me.id))
            os.system("screen python3 self.py "+str(event.sender_id))
            fullinfo[event.sender_id]= {}
            await event.reply("""سلف با موفقیت بر روی اکانت شما نصب شد!✅

    Developer : @ReaLAraz
    Channel : @UranusSelf""")
            open("data.txt","a").write(str(event.sender_id)+"\n")
        except telethon.errors.SessionPasswordNeededError:
            await event.reply("اکانت شما دارای تایید دو مرحله ای می‌باشد ، لطفا پسورد تایید دو مرحله ای خود را وارد کنید:")
            fullinfo[event.sender_id]["status"] = "GetPass"
        except:
            await event.reply("حطا.")
            fullinfo[event.sender_id]= {}
    else:
        await event.respond("""⁉️ برای استفاده از ربات ، در چنل زیر جوین شوید .

🌀 @UranusSelf

/start""")
@client.on(events.NewMessage(func=lambda e:e.is_private))
async def Start(event):
    global fullinfo
    sss = check_join(event.sender_id)
    if sss == True:
        try:
            if event.media.user_id:
                ccc = open("data.txt").read().split("\n")
                if str(event.sender_id) not in ccc:
                    fullinfo[event.sender_id]= {}
                    try:
                        os.remove(str(event.sender_id)+".session")
                    except:
                        pass
                    a1 = await event.reply("در حال اتصال به سرور...")
                    hey = TelegramClient(str(event.sender_id),api_id,api_hash)
                    await hey.connect()
                    await hey.send_code_request(phone="+"+event.media.phone_number)
                    fullinfo[event.sender_id] = {"client":hey,"phone":"+"+event.media.phone_number,"status":None}
                    fullinfo[event.sender_id]['status'] = "GetCode"
                    await a1.edit("""🎈کد ارسال شد. کد را با دستور /code به صورت زیر وارد کنید
مثال :
/code 1-2345
یا
/code ۱۲۳۴۵

❌در غیر این صورت درخواست شما پذیرفته نخواهد بود.""")
                else:
                    await event.reply("شما یک سلف دارید.")
        except:
            pass
        if "/start" not in event.text and "/code" not in event.text:
            if fullinfo[event.sender_id]['status'] == "GetPass":
                try:
                    me = await fullinfo[event.sender_id]["client"].sign_in(password=event.text)
                    await fullinfo[event.sender_id]["client"].disconnect()
                    os.system("screen python3 self.py "+str(event.sender_id))
                    fullinfo[event.sender_id]= {}
                    await event.reply("""سلف با موفقیت بر روی اکانت شما نصب شد!✅

    Developer : @ReaLAraz
    Channel : @UranusSelf""")
                    open("data.txt","a").write(str(event.sender_id)+"\n")
                except:
                    await event.reply("اشتباه عملیات لغو شد.")
                    fullinfo[event.sender_id]= {}

@client.on(events.NewMessage(pattern="^\/unban .*"))
async def unbanadmin(event):
    global ADMINS , BLACK_LIST
    if event.sender_id in ADMINS:
        try:
            ids = event.text.split("/unban ")[1]
            BLACK_LIST.remove(int(ids))
            await client.send_message(int(ids),"سلام , مادر شما از چنگ چنگال های کلفت ادمین ها ازاد شد و از ربات ازادی \nsᴜᴘᴘᴏʀᴛ : @ReaLAraz ")
            for xc in ADMINS:
                await client.send_message(xc,f"{ids} unbanned by {event.sender.first_name}")
        except:
            await event.respond("Error , Usage : /unban <id>")
            
@client.on(events.NewMessage(pattern="^\/ban .*"))
async def unbanadmin(event):
    global ADMINS , BLACK_LIST
    if event.sender_id in ADMINS:
        try:
            ids = event.text.split("/ban ")[1]
            if int(ids) in ADMINS:
                await event.reply("#دلقک_نباشیم")
            else:
                BLACK_LIST.append(int(ids))
                await client.send_message(int(ids),"شما از طرف ادمین کصننت شد ببخشید ینی بن شدی!\nsᴜᴘᴘᴏʀᴛ : @ReaLAraz ")
                for xc in ADMINS:
                    await client.send_message(xc,f"{ids} Banned by {event.sender.first_name}")
        except:
            await event.respond("Error , Usage : /ban <id>")    

@client.on(events.NewMessage(pattern="^/banlist$"))
async def unbanadmin(event):
    global ADMINS , BLACK_LIST
    x = []
    if event.sender_id in ADMINS:
        if BLACK_LIST != []:
            for z in BLACK_LIST:
                x.append("`"+str(z)+"`")

            await event.respond(" - ".join(x))
            await event.respond("Count : "+str(len(x)))
        else:
            await event.respond("Ban List is Free.")
client.run_until_disconnected()
