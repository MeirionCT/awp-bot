from xml.etree.ElementTree import tostring
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

from ossapi import Ossapi, UserLookupKey, RankingType, GameMode  # Python wrapper for the osu! API. Documentation: https://tybug.dev/ossapi/index.html

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
print(token)

# discord api stuff
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# create client
client_id = 48481
client_secret = "bsjuwhP1SRJ3b3qhD9iDraxnLoQOtc2KHsU9Ehe5"
api = Ossapi(client_id,client_secret)

top = api.ranking(GameMode.OSU, RankingType.PERFORMANCE)
print(top.ranking[0].user.username)
