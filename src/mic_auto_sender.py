import time
from screen import Microphone
from dotenv import load_dotenv
load_dotenv('.env')

microphone = Microphone()

while True:
    microphone.record()
    time.sleep(5)