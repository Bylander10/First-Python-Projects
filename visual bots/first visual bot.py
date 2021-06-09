from time import sleep

import keyboard
import pyautogui
import win32api
import win32con


# Tile 1 Position X:  256 Y:  626 RGB: (197,  98, 117)
# Tile 2 Position X:  326 Y:  626 RGB: (196,  98, 117)
# Tile 3 Position X:  399 Y:  626 RGB: (164,  65,  70)
# Tile 4 Position X:  466 Y:  626 RGB: (204, 105, 118)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


sleep(3)
while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(256, 626)[0] == 0:
        click(581, 400)
    if pyautogui.pixel(326, 626)[0] == 0:
        click(682, 400)
    if pyautogui.pixel(399, 626)[0] == 0:
        click(770, 400)
    if pyautogui.pixel(466, 626)[0] == 0:
        click(869, 400)
