from PIL.ImageOps import grayscale
from sys import stdin
import pyautogui

cnt = 0;
f = open("in.txt")
for url in f:
    print("Adding " + url)
    now = pyautogui.locateOnScreen('new_tab.png', grayscale = True, confidence = .8)
    pyautogui.click(x = now.left , y = now.top)
    pyautogui.write(url)
    pyautogui.hotkey('enter')
    now = None
    while now is None:
        now = pyautogui.locateOnScreen('add.png', grayscale = True, confidence = .8)
        # print(now)
    pyautogui.click(x = now.left, y = now.top)
    now = None
    while now is None:
        now = pyautogui.locateOnScreen('list.png', grayscale = True, confidence = .8)
        # print(now)
    pyautogui.click(x = now.left + 20, y = now.top + 20, duration = 0.25)
    cnt = cnt + 1
    print("Added " + str(cnt) + " by now")


