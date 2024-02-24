import pyautogui
import time
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from dotenv import load_dotenv

class Screenshot():
    def __init__(self):
        self.name = ""

    def printscreen(self):
        self.name = f"files\\{time.strftime('%m-%d_%H-%M-%S')}.png"
        screenshot = pyautogui.screenshot(allScreens=True)
        screenshot.save(self.name)

class Microphone():
    def __init__(self):
        self.sample_rate =  44100
        self.duration =  5.0 # 5 sec for testing, normally 180
        self.recording = None
        self.process_time = 0
        self.name = ""

    def record(self):
        self.name = f"files\\{time.strftime('%m-%d_%H-%M-%S')}.wav"
        self.recording = sd.rec(int(self.duration * self.sample_rate), samplerate=self.sample_rate, channels=2)
        time.sleep(self.duration)
        start_time = time.time()
        sd.stop()
        sd.wait()
        wav.write(self.name, self.sample_rate, self.recording)
        end_time = time.time()
        self.process_time = end_time - start_time