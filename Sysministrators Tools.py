import pyautogui
import time
import keyboard
import random

region = pyautogui.screenshot()
screen_width, screen_height = region.size

regx = 0
regy = 0
regw = 0
regh = 0

if screen_width == 1920 and screen_height == 1080:
    regx = 680
    regy = 290
    regw = 520
    regh = 620

if screen_width == 2560 and screen_height == 1440:
    regx = 900
    regy = 340
    regw = 900
    regh = 600

while 1:

    while keyboard.is_pressed('shift') == True:

        pic = pyautogui.screenshot(region=(regx, regy, regw, regh))
        width, height = pic.size

        for x in range(0, width, 5):
            for y in range(0, height, 5):
                r, g, b = pic.getpixel((x, y))
                randomizex = x + random.uniform(1,25)
                randomizey = y + random.uniform(1,6)

                if r in range(0,3) and g in range(116,121):
                    pyautogui.moveTo(randomizex+900, randomizey+340, duration=0.1)
                    print("Item located at " + (str(x)) + "," + (str(y)) + "," + (str(pic.getpixel((x,y)))))
                    time.sleep(0.05)
                    break
            else:
                continue
            break
