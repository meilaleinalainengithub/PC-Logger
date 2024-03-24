import os, sqlite3
from datetime import datetime
    


if __name__ == "__main__":
    data = []
    data = execute()
    
    with open("files\\history.txt", "a") as file:
        for url in data:
            file.write(url)
