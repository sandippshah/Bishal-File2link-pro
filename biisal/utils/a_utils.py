import pytz, random, string  
from datetime import datetime, date, time, timedelta
from biisal.vars import Var
from shortzy import Shortzy
from biisal.utils.database import Database
from biisal.utils.database import db
db = Database(Var.DATABASE_URL, Var.name)
import logging
from pyrogram.errors import InputUserDeactivated, UserNotParticipant, FloodWait, UserIsBlocked, PeerIdInvalid



from imdb import Cinemagoer 
import asyncio
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait, UserIsBlocked, MessageNotModified, PeerIdInvalid
from pyrogram import enums
from typing import Union
import pytz
import random 
import re
import os
from datetime import datetime, date, time, timedelta
import string
from typing import List
from bs4 import BeautifulSoup
import requests
import aiohttp
from shortzy import Shortzy
import http.client
import json





logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

BTN_URL_REGEX = re.compile(
    r"(\[([^\[]+?)\]\((buttonurl|buttonalert):(?:/{0,2})(.+?)(:same)?\))"
)



BANNED = {}
VERIFY = {}
TOKENS = {}
VERIFIED = {}


class temp(object):
    GETALL = {}
    SHORT = {}
    SETTINGS = {}
    IMDB_CAP = {}
    VERIFY = {}
    TOKENS = {}
    VERIFIED = {}



async def get_verify_shorted_link(link):
    shortzy = Shortzy(api_key=Var.SHORT_API, base_site=Var.SHORT_URL)
    link = await shortzy.convert(link)
    return link

async def check_token(bot, userid, token):
    user = await bot.get_users(userid)
    if user.id in TOKENS.keys():
        TKN = TOKENS[user.id]
        if token in TKN.keys():
            is_used = TKN[token]
            if is_used == True:
                return False
            else:
                return True
    else:
        return False

async def get_token(bot, userid, link):
    user = await bot.get_users(userid)
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
    TOKENS[user.id] = {token: False}
    link = f"{link}verify-{user.id}-{token}"
    shortened_verify_url = await get_verify_shorted_link(link)
    return str(shortened_verify_url)


async def get_verify_status(userid):
    status = temp.VERIFY.get(userid)
    if not status:
        status = await db.get_verified(userid)
        temp.VERIFY[userid] = status
    return status

async def update_verify_status(userid, date_temp, time_temp):
    status = await get_verify_status(userid)
    status["date"] = date_temp
    status["time"] = time_temp
    temp.VERIFY[userid] = status
    await db.update_verification(userid, date_temp, time_temp)
    
        
async def verify_user(bot, userid, token):
    user = await bot.get_users(int(userid))
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id, user.first_name)
        await bot.send_message(
            Var.NEW_USER_LOG,
            f"**New User Joined:** \n\n__My new friend__ [{user.mention}](tg://user?id={user.id}) __started your bot!__\nBot : @{Var.BOT_USERNAME}"
        )
        
        
    TOKENS[user.id] = {token: True}
    tz = pytz.timezone('Asia/Kolkata')
    date_var = datetime.now(tz)+timedelta(hours=12) #added verification expire Time. in Hour 12hours 
    temp_time = date_var.strftime("%H:%M:%S")
    date_var, time_var = str(date_var).split(" ")
    await update_verify_status(user.id, date_var, temp_time)    
    
                
async def check_verification(bot, userid):
    user = await bot.get_users(int(userid))
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id, user.first_name)
        await bot.send_message(
            Var.NEW_USER_LOG,
            f"**New User Joined:** \n\n__My new friend__ [{user.mention}](tg://user?id={user.id}) __started your bot!__\nBot : @{Var.BOT_USERNAME}"
        )
        # premium verification bypass added 
    if await db.has_premium_access(user.id):
        return True      
    else:
        pass
    if user.id in Var.ADMINS:
        return True
    else:
        pass       
    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    now = datetime.now(tz)
    curr_time = now.strftime("%H:%M:%S")
    hour1, minute1, second1 = curr_time.split(":")
    curr_time = time(int(hour1), int(minute1), int(second1))
    status = await get_verify_status(user.id)
    date_var = status["date"]
    time_var = status["time"]
    years, month, day = date_var.split('-')
    comp_date = date(int(years), int(month), int(day))
    hour, minute, second = time_var.split(":")
    comp_time = time(int(hour), int(minute), int(second))
    if comp_date<today:
        return False
    else:
        if comp_date == today:
            if comp_time<curr_time:
                return False
            else:
                return True
        else:
            return True                                        
            
async def get_seconds(time_string):
    def extract_value_and_unit(ts):
        value = ""
        unit = ""

        index = 0
        while index < len(ts) and ts[index].isdigit():
            value += ts[index]
            index += 1

        unit = ts[index:].lstrip()

        if value:
            value = int(value)

        return value, unit

    value, unit = extract_value_and_unit(time_string)

    if unit == 's':
        return value
    elif unit == 'min':
        return value * 60
    elif unit == 'hour':
        return value * 3600
    elif unit == 'day':
        return value * 86400
    elif unit == 'month':
        return value * 86400 * 30
    elif unit == 'year':
        return value * 86400 * 365
    else:
        return 0                