import pyautogui
import time
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from dotenv import load_dotenv

class Screenshot():
    def __init__(self):
        self.nameadd = 0
        self.name = ""

    def printscreen(self):
        self.nameadd +=  1
        self.name = f"files\\{time.strftime('%m-%d_%H-%M-%S')}.png"
        screenshot = pyautogui.screenshot(allScreens=True)
        screenshot.save(self.name)
    
    def update_env(self, key, value):
        load_dotenv(".env")

        with open('.env', 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.startswith(f"{key}="):
                lines[i] = f"{key}={value}\n"
                break

        with open('.env', 'w') as file:
            file.writelines(lines)

class Microphone():
    def __init__(self):
        self.sample_rate =  44100
        self.duration =  60.0
        self.recording = None
        self.process_time = 0
        self.nameadd = 0
        self.name = ""

    def record(self):
        self.nameadd += 1
        self.name = f"files\\{time.strftime('%m-%d_%H-%M-%S')}.png"
        self.recording = sd.rec(int(self.duration * self.sample_rate), samplerate=self.sample_rate, channels=2)
        time.sleep(self.duration)
        start_time = time.time()
        sd.stop()
        sd.wait()
        wav.write(self.name, self.sample_rate, self.recording)
        end_time = time.time()
        self.process_time = end_time - start_time

    def update_env(self, key, value):
        load_dotenv(".env")

        with open('.env', 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.startswith(f"{key}="):
                lines[i] = f"{key}={value}\n"
                break

        with open('.env', 'w') as file:
            file.writelines(lines)