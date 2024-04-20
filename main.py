from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
import requests 

#aşağıdakı 3 sətrin " " içində yazacağınız bölümünü
# my.telegram.org saytına daxil olaraq
# api development tools dan götürə bilərsiniz.
api_id = " "
api_hash = " "
bot_token = "  "


app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


# start və check əmri bölümü
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Salam! Axtarmaq istədiyiniz istifadəçinin adını /check əmri ilə yazın.")


@app.on_message(filters.command("check"))
async def check(client, message):
    if len(message.command) < 2:
        await message.reply_text("İstifadə: /check username")
        return
    username = message.command[1]
    result = check_username(username)
    await message.reply_text(result)


def check_username(username):
    sites = {
        "Facebook": f"https://www.facebook.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "YouTube": f"https://www.youtube.com/{username}",
        "Telegram":f"https://t.me/{username}",
        "Twitter":f"https://twitter.com/{username}",
        "Instagram":f"https://instagram.com/{username}",
        "Snapchat":f"https://www.snapchat.com/add/{username}",
        "Pinterest":f"https://tr.pinterest.com/{username}",
        "Linkedin":f"https://www.linkedin.com/in/{username}",
        # əlavələrinizi yuxarıdakılara uyğun edə bilərsiniz.
    }
    
    # nəticələri çıxarıb istifadəçiyə göndərmək üçün bölüm 
    results = []
    for site, url in sites.items():
        response = requests.get(url)
        if response.status_code == 200:
            results.append(f"✅{site} tapıldı: {url}✅")
        else:
            results.append(f"⚠️{site} tapılmadı⚠️")
    
    return "\n".join(results)

app.run()
