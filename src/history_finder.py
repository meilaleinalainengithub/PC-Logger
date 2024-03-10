import os

def get_user():
    return os.getlogin()

filedirs = [
    f"C:\\Users\\{get_user()}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History",
    f"C:\\Users\\{get_user()}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\History",
    f"C:\\Users\\{get_user()}\\Roaming\\Opera Software\\Opera GX Stable\\History",
    f"C:\\Users\\{get_user()}\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\History"
]

class SearchHistory():
    def __init__(self):
        self.user = get_user()

    def get_all():
        for filedir in filedirs:
            if os.path.exists(filedir):
                with open(filedir, "r") as file:
                    return file.read()
            else:
                return None
        
    def get_chrome():
        if os.path.exists(filedirs[0]):
            with open(filedirs[0], "r") as file:
                return file.read
        else:
            return None
    
    def get_brave():
        if os.path.exists(filedirs[1]):
            with open(filedirs[1], "r") as file:
                return file.read
        else:
            return None
    
    def get_opera():
        if os.path.exists(filedirs[2]):
            with open(filedirs[2], "r") as file:
                return file.read
        else:
            return None
    
    def get_edge():
        if os.path.exists(filedirs[3]):
            with open(filedirs[3], "r") as file:
                return file.read
        else:
            return None