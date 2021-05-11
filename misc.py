import pyautogui
import time
import keyboard
import random

class Misc:

    def setregion(self):
        region = pyautogui.screenshot()
        screen_width, screen_height = region.size

        if screen_width == 1920 and screen_height == 1080:
            regx = 680
            regy = 290
            regw = 520
            regh = 620
            return regx, regy, regw, regh

        if screen_width == 2560 and screen_height == 1440:
            regx = 900
            regy = 340
            regw = 900
            regh = 600
            return regx, regy, regw, regh

    def bvskilltoggle(self):

        skilltoggle = False
        unleashcd = 1 + (random.uniform(0.01, 0.05))
        unleashtoggle = 'l'
        unleashhotkey = 'r'

        while 1:

            if keyboard.is_pressed('ctrl') == True and keyboard.is_pressed(unleashtoggle) == True:
                print(str(skilltoggle))
                skilltoggle = not skilltoggle
                print('Key pressed.' + ' Current status of toggle:' + str(skilltoggle))

            while skilltoggle == True:
                keyboard.press_and_release(unleashhotkey)
                time.sleep(unleashcd * 3)
                if keyboard.is_pressed(unleashtoggle) == True:
                    skilltoggle = not skilltoggle
                    print('Key pressed again. Breaking Loop')
                    time.sleep(5)
