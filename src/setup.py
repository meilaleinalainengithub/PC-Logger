import os, easygui
from dotenv import load_dotenv
load_dotenv()

def exists_false():
    req = []
    for i in keys:
        if os.getenv(i) == "":
            req.append(i)
    
    for i in req:
        key = easygui.enterbox(f"THIS PROGRAM IS MISSING: {i}.\nPLEASE ENTER IT HERE:")
        os.environ[i] = key

if __name__ == "__main__":
    keys = ['TOKEN', 'LOGGER_CHANNEL_ID', 'SERVER_ID', 'SCREENSHOT_CHANNEL_ID', 'MICROPHONE_CHANNEL_ID', 'COMMANDS_CHANNEL_ID', 'STATUS_CHANNEL_ID']
    while True:
        if os.path.exists("\\PC-Logger\\.env"):
            if os.getenv('TOKEN') != "NONE" and os.getenv('SERVER_ID') != "NONE" and os.getenv('SCREENSHOT_CHANNEL_ID') != "NONE" and os.getenv('MICROPHONE_CHANNEL_ID') != "NONE" and os.getenv('COMMANDS_CHANNEL_ID') != "NONE" and os.getenv('STATUS_CHANNEL_ID') != "NONE":
                break
            else:
                exists_false()
        else:
            with open("\\PC-Logger\\.env", "w") as env_file:
                for key in keys:
                    env_file.write(f"{key}='NONE'\n")