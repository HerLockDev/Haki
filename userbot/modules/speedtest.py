from datetime import datetime

from speedtest import Speedtest
from telethon import functions
from userbot import CMD_HELP
from userbot.events import register
from userbot.cmdhelp import CmdHelp
import os
from requests import get

@register(outgoing=True, pattern="^.cspeedtest$")
@register(outgoing=True, pattern="^.cspeed$")
async def cspeedtstimg(spd):
    test = Speedtest()
    MESSAGE = ""
    try:
        await spd.edit("`Hız testi için sunucu bilgisi getiriliyor...`")
        test.get_best_server()
    except:
        await spd.edit("`Hız testi için sunucu bilgisi tekrar getiriliyor...`")
        try:
            test.get_best_server()
        except:
            return await spd.edit("`Hız testi için sunucu bilgileri getirilemedi!`")

    MESSAGE = "**Sunucu:** `"+test.results.server['sponsor']+"("+test.results.server['name']+")`"
    await spd.edit(MESSAGE + "\n**İndirme Hızı**: `Test yapılıyor...`")
    test.download()
    MESSAGE += "\n**İndirme Hızı**: `"+"%0.2f Mbit/s`" % (float(test.results.dict()['download'])  / 1000.0 / 1000.0)
    await spd.edit(MESSAGE + "\n**Yükleme Hızı**: `Test yapılıyor...`")
    test.upload()
    MESSAGE += "\n**Yükleme Hızı**: `"+"%0.2f Mbit/s`" % (float(test.results.dict()['upload']) / 1000.0 / 1000.0)
    MESSAGE += "\n**Ping**: `"+"%0.3f ms`" % float(test.results.dict()['ping'])
    MESSAGE += "\n**ISP**: "+ "`%s`" % str(test.results.dict()['client']['isp'])
    await spd.edit(MESSAGE + "\n`Test bilgisi hazırlanıyor...`")
    test.results.share()
    if os.path.exists("@MiaUserBot-Cspeed.jpg"):
        os.remove("@MiaUserBot-Cspeed.jpg")

    try:
        r = get(test.results.share())
        with open("@MiaUserBot-Cspeed.jpg", 'wb') as f:
            f.write(r.content)    
        await spd.client.send_file(spd.chat_id, file="@MiaUserBot-Cspeed.jpg", force_document=False, caption=MESSAGE)
        os.remove("@MiaUserBot-Cspeed.jpg")
        await spd.delete()
    except:
        await spd.edit(MESSAGE)


CmdHelp('cspeedtest').add_command(
    'cspeedtest', None, 'Hız testi yapar ve gelişmiş ve resimli şekilde bilgileri gösterir.'
).add()
