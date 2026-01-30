import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

from ossapi import Ossapi, RankingType, GameMode

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# discord api stuff
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# create client
client_id = 3852530
client_secret = 1
api = Ossapi(client_id,client_secret)

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"My penis hurt, {bot.user.name}")

@bot.event
async def on_message(message):
        if message.author == bot.user:
            return
        if "arrecio" in message.content.lower():
            await message.channel.send("Que hace mucho frio")

        await bot.process_commands(message)

top50 = api.ranking(GameMode.OSU, RankingType.PERFORMANCE)
print(top50.ranking[0].user.username)
bot.run(token, log_handler=handler, log_level=logging.DEBUG)
