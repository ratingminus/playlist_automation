from PIL.ImageOps import grayscale
from sys import stdin
from numpy import add
import pyautogui

cnt = 0;
f = open("in.txt")
g = open("out.txt", "a")
h = open("done.txt", "a")
k = open("done.txt", "r")

for url in f:
    if url in k:
        continue
    print("Adding " + url)
    now = pyautogui.locateOnScreen('new_tab.png', grayscale = False, confidence = .8)
    pyautogui.click(x = now.left , y = now.top)
    pyautogui.write(url)
    pyautogui.hotkey('enter')
    if_kids = None
    for i in range(30):
        if_kids = pyautogui.locateOnScreen('kids.png', grayscale = False, confidence = 0.8)
    if if_kids != None:
        g.write("\n" + url)
        continue
    save_now = None
    while save_now is None:
        save_now = pyautogui.locateOnScreen('save.png', grayscale = False, confidence = .8)
        print("wtf")
    print(save_now)
    pyautogui.click(x = save_now.left, y = save_now.top)
    add_now = None
    while add_now is None:
        add_now = pyautogui.locateOnScreen('add_testing.png', grayscale = False, confidence = .8)
    print(add_now)
    pyautogui.click(x = add_now.left, y = add_now.top, duration = 0.25)
    cnt = cnt + 1
    print("Added " + str(cnt) + " by now")
    h.write("\n" + url)


