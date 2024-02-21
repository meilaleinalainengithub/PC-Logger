from screen import Screenshot
import time
import os

screenshot = Screenshot()

count = 0
determine = count + 1
while True:
    screenshot.printscreen()
    count += 1
    if count >= determine:
        # screenshot.update_env('runMic', "True")

        screenshot_path = screenshot.name
        os.remove(screenshot_path) # COMMENT OUT IF YOU WANT TO KEEP IT
        determine += 1
    time.sleep(3)