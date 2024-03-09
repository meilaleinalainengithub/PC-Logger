import time
from screen import Microphone

microphone = Microphone()
while True:
    microphone.record()
    time.sleep(5)