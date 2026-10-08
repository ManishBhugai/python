import pyautogui
import time

time.sleep(5)
count=100
for i in range(count):
    pyautogui.typewrite("Sorry for spamming")
    pyautogui.press('enter')
    time.sleep(0.4)