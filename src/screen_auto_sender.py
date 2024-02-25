import time
from screen import Screenshot
from dotenv import load_dotenv
load_dotenv('.env')

screenshot = Screenshot()

while True:
    screenshot.printscreen()
    time.sleep(3)