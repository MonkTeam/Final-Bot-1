#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) gautamajay52

import subprocess
import os
import asyncio

from tobrot import (
    EDIT_SLEEP_TIME_OUT,
    DESTINATION_FOLDER,
    RCLONE_CONFIG
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


async def check_size_g(client, message):
    #await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
    del_it = await message.reply_text("🔊 𝘾𝙝𝙚𝙘𝙠𝙞𝙣𝙜 𝙨𝙞𝙯𝙚...𝙬𝙖𝙞𝙩!!!")
    if not os.path.exists('rclone.conf'):
        #subprocess.Popen(('touch', 'rclone.conf'), stdout = subprocess.PIPE)
        with open('rclone.conf', 'a', newline="\n", encoding = 'utf-8') as fole:
            fole.write("[DRIVE]\n")
            fole.write(f"{RCLONE_CONFIG}")
    destination = f'{DESTINATION_FOLDER}'
    cmd = ['rclone', 'size', '--config=./rclone.conf', 'DRIVE:'f'{destination}']
    gau_tam = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    gau, tam = await gau_tam.communicate()
    print(gau)
    print(tam)
    print(tam.decode("utf-8"))
    gautam = gau.decode("utf-8")
    print(gautam)
    await asyncio.sleep(5)
    await message.reply_text(f"🔊𝘾𝙡𝙤𝙪𝙙𝙄𝙣𝙛𝙤:\n\n{gautam}")
    await del_it.delete()

#gautamajay52

async def g_clearme(client, message):
    inline_keyboard = []
    ikeyboard = []
    ikeyboard.append(InlineKeyboardButton("𝙔𝙚𝙨 🚫", callback_data=("fuckingdo").encode("UTF-8")))
    ikeyboard.append(InlineKeyboardButton("𝙉𝙤 🤗", callback_data=("fuckoff").encode("UTF-8")))
    inline_keyboard.append(ikeyboard)
    reply_markup = InlineKeyboardMarkup(inline_keyboard)
    await message.reply_text("𝘼𝙧𝙚 𝙮𝙤𝙪 𝙨𝙪𝙧𝙚? 🚫 𝙏𝙝𝙞𝙨 𝙬𝙞𝙡𝙡 𝙙𝙚𝙡𝙚𝙩𝙚 𝙖𝙡𝙡 𝙮𝙤𝙪𝙧 𝙙𝙤𝙬𝙣𝙡𝙤𝙖𝙙𝙨 𝙡𝙤𝙘𝙖𝙡𝙡𝙮 🚫", reply_markup=reply_markup, quote=True)
