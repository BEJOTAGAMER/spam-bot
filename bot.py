import pyautogui
import time

f = open("spam.txt", "r")
time.sleep(60)
for words in f:
    print(words)
    pyautogui.typewrite(words)
    pyautogui.press("enter")
    time.sleep(3)
