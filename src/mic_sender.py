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
            runMic = True
            os.environ['runMic'] = runMic
            os.environ['mïcCount'] = count

            mic_path = f"files\\{count}.wav"       
            os.remove(mic_path) # COMMENT OUT IF YOU WANT TO KEEP IT
            determine += 1
        time.sleep(3)
        