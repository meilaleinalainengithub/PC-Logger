import pyautogui
import time
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from dotenv import load_dotenv

class Screenshot():
    def __init__(self):
        self.nameadd = 0

    def printscreen(self):
        self.nameadd +=  1
        screenshot = pyautogui.screenshot(allScreens=True)
        screenshot.save(f"files\\{self.nameadd}.png")
    
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

    def record(self):
        self.nameadd += 1
        self.recording = sd.rec(int(self.duration * self.sample_rate), samplerate=self.sample_rate, channels=2)
        time.sleep(self.duration)
        start_time = time.time()
        sd.stop()
        sd.wait()
        wav.write(f"files\\{self.nameadd}.wav", self.sample_rate, self.recording)
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
            