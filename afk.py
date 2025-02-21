from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

while True:
    keyboard.press('a')
    keyboard.release('a')

    time.sleep(2)

    keyboard.press('s')
    keyboard.release('s')

    time.sleep(2)