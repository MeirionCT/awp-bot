print("1")
from xml.etree.ElementTree import tostring
print("2")
import discord
print("3")
from discord.ext import commands
print("4")
import logging
print("5")
from dotenv import load_dotenv
print("6")
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

bot = commands.Bot(command_prefix='!', intents=intents)

#@bot.event
#async def on_ready():
#    print(f"Test message here, {bot.user.name}")

#@bot.event
#async def on_message(message):
#       if message.author == bot.user:
#           return
#       if "arrecio" in message.content.lower():
#            await message.channel.send("Que hace mucho frio")
#        await bot.process_commands(message)


#@bot.command()
#async def rank(ctx, arg):
#    await ctx.send(arg)


top = api.ranking(GameMode.OSU, RankingType.PERFORMANCE)
print(top.ranking[0].user.username)
#bot.run(token, log_handler=handler, log_level=logging.DEBUG)
