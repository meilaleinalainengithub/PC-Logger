import os, sqlite3, psutil

class SearchHistory():
    def __init__(self):
        self.user = self.get_user()
        self.database = None
        self.self.filedirs = [
    f"C:\\Users\\{self.get_user()}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History",
    f"C:\\Users\\{self.get_user()}\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\History",
    f"C:\\Users\\{self.get_user()}\\Roaming\\Opera Software\\Opera GX Stable\\History",
    f"C:\\Users\\{self.get_user()}\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\History"]

    def get_user(self):
        return os.getlogin()

    def execute(self):
        data = []
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
                pass
            else:
                return None
        
    def get_chrome(self):
        if os.path.exists(self.filedirs[0]):
            self.database = self.filedirs[0]
        else:
            return None
    
    def get_brave(self):
        if os.path.exists(self.filedirs[1]):
            self.database = self.filedirs[1]
        else:
            return None
    
    def get_opera(self):
        if os.path.exists(self.filedirs[2]):
            self.database = self.filedirs[2]
        else:
            return None
    
    def get_edge(self):
        if os.path.exists(self.filedirs[3]):
            self.database = self.filedirs[3]
        else:
            return None
        

SearchHistory = SearchHistory()
result = SearchHistory.get_chrome()
print(result)