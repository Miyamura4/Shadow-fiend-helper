import threading
import time
import keyboard
import mouse
import pyautogui

print("wassup homie look at my Shadow Fiend helper")


def arcane(bind):
    while True:
        if keyboard.is_pressed(bind):
            pyautogui.press('1')
            time.sleep(0.2)
            mouse.click('left')
            time.sleep(1.20)
            print("casting requiem...")
            pyautogui.press('r')
            print("======================")
            print("Enemy is exploded.")


def base(binds):
    while True:
        if keyboard.is_pressed(binds):
            pyautogui.press('1')
            time.sleep(0.1)
            mouse.click('left')
            time.sleep(0.80)
            print("casting requiem...")
            pyautogui.press('r')
            print("======================")
            print("Enemy is exploded.")


das = input("Tell me about your requiem(with yasha and kaya = 0/without = 1): ")
das = int(das)
if das == 0:
    bind = input("Type your bind button here: ")
    thread1 = threading.Thread(target=arcane(bind))
    thread1.start()
else:
    binds = input("Type your bind button here: ")
    thread2 = threading.Thread(target=base(binds))
    thread2.start()
    thread2.join()
