import json
import urllib.request
from userbot.events import register 
from userbot.cmdhelp import CmdHelp 

@register(outgoing=True, pattern=".ipbilgi (.*)") 
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    adress = input_str
    token = "19e7f2b6fe27deb566140aae134dec6b" 
    api = "http://api.ipstack.com/" + adress + "?access_key=" + token + "&format=1" 

    result = urllib.request.urlopen(api).read()
    result = result.decode()
# siteye göre ayarlı
    result = json.loads(result)
    a = result["type"] 
    b = result["country_code"]
    c = result["region_name"]
    d = result["city"]
    e = result["zip"]
    f = result["latitude"]
    await event.edit("**Verdiğiniz ip adresinden bilgileri arıyorum...** 👀")
    await event.edit(
        f"<b><u>Mia UserBot Modülü</b></u>\n\n<b>IP tipi :-</b><code>{a}</code>\n<b>Ülke kodu:- </b> <code>{b}</code>\n<b>Devlet adı :-</b><code>{c}</code>\n<b>Şehir adı :- </b><code>{d}</code>\n<b>Posta kodu :-</b><code>{e}</code>\n<b>Adres kordinatı:- </b> <code>{f}</code>",
        parse_mode="HTML")

CmdHelp("ipbilgi").add_command('ipbilgi', "{IP adress yazin}", "yazdiginiz ip adressine göre yer tespiti yapar.").add()
