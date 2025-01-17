# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

from datetime import datetime

from speedtest import Speedtest
from time import sleep
from userbot import CMD_HELP, StartTime, ALIVE_NAME
from userbot.events import register
import time


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Running high speed test . . .`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("`"
                   "Started at "
                   f"{result['timestamp']} \n\n"
                   "Download "
                   f"{speed_convert(result['download'])} \n"
                   "Upload "
                   f"{speed_convert(result['upload'])} \n"
                   "Ping "
                   f"{result['ping']} \n"
                   "ISP "
                   f"{result['client']['isp']}"
                   "`")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**▁**")
    await pong.edit("**▂▁**")
    await pong.edit("**▃▂▁**")
    await pong.edit("**▄▃▂▁**")
    await pong.edit("**▅▄▃▂▁**")
    await pong.edit("**▇▅▄▃▂▁**")
    await pong.edit("**▇▆▅▄▃▂▁**")
    await pong.edit("**█▇▆▅▄▃▂▁**")
    await pong.edit("⚡")
    sleep(2)
    await pong.edit("**PING!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**ㅤㅤㅤ  ≛ 𝙲𝙾𝚁𝙾𝙽𝙰 𝚅𝙸𝚁𝚄𝚂 ≛** \n ㅤ**▰▱▰▱▰▱▰▱▰▱▰▱▰** \n╭╼═════════════════╾╮\n⌲Ping Virus  :  %s𝖒𝖘\n⌲Virus Aktif  :  {uptime} 𝐎𝐍⊨〛\n⌲My Boss   : ㅤ`{ALIVE_NAME}`\n╰╼═════════════════╾╯ " % (duration))              



@register(outgoing=True, pattern="^.sping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**𝐕**")
    await pong.edit("**𝐕𝐈**")
    await pong.edit("**𝐕𝐈𝐑**")
    await pong.edit("**𝐕𝐈𝐑𝐔**")
    await pong.edit("**𝐕𝐈𝐑𝐔𝐒**")
    await pong.edit("⚡")
    sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**𖣘PING𖣘 **\n ➟%s𝖒𝖘\n**𖣘TIME AKTIF𖣘**\n ➟ {uptime} DANGER" % (duration))
    


@register(outgoing=True, pattern="^.pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`GASPOL!!!`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit("`Ping!\n%sms`" % (duration))

CMD_HELP.update(
    {"ping": "`.ping`\
    \nUsage: Shows how long it takes to ping your bot.\
    \n\n`.speed`\
    \nUsage: Does a speedtest and shows the results.\
    \n\n`.sping`\
    \nUsage: melihat kecepatan ping dengan tampilan lain.\
    \n\n`.pong`\
    \nUsage: Shows how long it takes to ping your bot."
     })
