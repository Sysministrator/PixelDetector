import pyautogui
import keyboard

# Any duration less than this is rounded to 0.0 to instantly move the mouse.
pyautogui.MINIMUM_DURATION = 0.02  # Default: 0.1
# Minimal number of seconds to sleep between mouse moves.
pyautogui.MINIMUM_SLEEP = 0.02  # Default: 0.05
# The number of seconds to pause after EVERY public function call.
pyautogui.PAUSE = 0.02  # Default: 0.1

# Define Variables
runOnce = True
regx = 0
regy = 0
regw = 0
regh = 0
mousePos = 0


# Set bounding box
def bbox():
    global regx
    global regy
    global regw
    global regh

    region = pyautogui.screenshot()
    screen_width, screen_height = region.size

    if screen_width == 1920 and screen_height == 1080:
        regx = 680
        regy = 290
        regw = 520
        regh = 620

    if screen_width == 2560 and screen_height == 1440:
        regx = 900
        regy = 340
        regw = 900
        regh = 700


# Functions to run only once
while runOnce:
    bbox()
    runOnce = False
    print('Bounding box set to: ' + str(regx), str(regh))


# Pixel search function
def pixelSearch():

    global mousePos
    pic = pyautogui.screenshot(region=(regx, regy, regw, regh))
    width, height = pic.size

    # Iterate through the bounding box looking for a specific color
    for x in range(0, width, 5):
        for y in range(0, height, 5):
            r, g, b = pic.getpixel((x, y))

            # Run this logic if the pixel is found within the bounding box
            if 0 <= r <= 2 and 116 <= g <= 119:
                pyautogui.moveTo(x + regx, y + regy)

                # Determine is the mouse position has moved. Update the mouse position if it has. Click if it has not.
                if mousePos != pyautogui.position():
                    mousePos = pyautogui.position()
                    #print('Mouse position updated.')
                else:
                    pyautogui.leftClick(x + regx, y + regy)
                    print('Mouse Clicked.')
                break
        else:
            continue
        break


while 1:

    while keyboard.is_pressed('shift'):
        pixelSearch()