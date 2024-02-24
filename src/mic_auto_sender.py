import os
import time
from screen import Microphone
from dotenv import load_dotenv
load_dotenv('.env')

microphone = Microphone()

while True:
    microphone.record()  
    microphone.modify_env("runMic", True)

    while runMic:
        time.sleep(0.1)
        runMic = os.getenv("runMic")
    
    time.sleep(5)