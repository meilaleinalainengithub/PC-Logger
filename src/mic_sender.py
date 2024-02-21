from screen import Microphone
import time
import os

microphone = Microphone()

count = 0
determine = count + 1
while True:
    microphone.record()
    count += 1
    if count >= determine:
        microphone.update_env('runMic', "True")

        mic_path = microphone.name   
        os.remove(mic_path) # COMMENT OUT IF YOU WANT TO KEEP IT
        determine += 1
    time.sleep(3)  