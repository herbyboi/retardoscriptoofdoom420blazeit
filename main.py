import random
import time

import win32gui
import win32api
import cv2
import mouse
img = cv2.imread('glimmer.png',cv2.IMREAD_UNCHANGED)
dc = win32gui.GetDC(0)
height, width, channels = img.shape







how_much_memory_can_you_offer = 1


def pigeonspawn():
    for i in range(how_much_memory_can_you_offer):
        offset_x, offsset_y = x + random.randint(1, 40), y + random.randint(1, 40)
        for i in range(height):
            for ii in range(width):
                r, g, b, a = img[i][ii][2], img[i][ii][1], img[i][ii][1], img[i][ii][3]
                if a > 0:
                    clr = win32api.RGB(r, g, b)
                    win32gui.SetPixel(dc, offset_x + ii, offsset_y + i, clr)

        time.sleep(0.5)
toggle=False
while 1:
    x,y = mouse.get_position()
    if mouse.is_pressed('right'):
        toggle = not toggle
    if toggle:
        time.sleep(1)
        print('yo')
        pigeonspawn()


