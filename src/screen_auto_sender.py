import time
from screen import Screenshot

screenshot = Screenshot()
while True:
    screenshot.printscreen()
    time.sleep(3)