import keyboard, time
import pynput.keyboard as kb

# gotta fix key_release to be detected

key_press_start_time = None
key_press_key = None
time_pressed = None

def key_release(key):
    global time_pressed
    elapsed_time = time.time() - key_press_start_time

    if elapsed_time <=  0.5:
        return 0
    else:
        time_pressed = elapsed_time

def key_press(key):
    global key_press_start_time
    global key_press_key
    key_press_start_time = time.time()
    key_press_key = key

def listen():
    full_data = []
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >=  5:
            return full_data  

        with kb.Listener(
            on_press=key_press,
            on_release=key_release) as listener:
            listener.join()

        # time_pressed, key = key_press(event, time.time())
        keydata = f"{key_press_key}: Pressed for: {time_pressed:.2f}s - {time.strftime('%m/%d %H:%M:%S')}\n"
        full_data.append(keydata)

if __name__ == "__main__":
    while True:
        with open('files\\keys.txt', "w") as file:
            pass

        full_data = listen()

        with open('files\\keys.txt', "r") as file:
            old_keys = file.readlines()

        with open('files\\keys.txt', "w") as file:
            file.writelines(old_keys + full_data)
