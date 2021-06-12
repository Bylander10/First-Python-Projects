from time import sleep
import pyautogui
import keyboard

import win32api, win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    sleep(0.08)


while not keyboard.is_pressed('c'):
    sc = pyautogui.screenshot(region=(58, 241, 599, 420))
    width, height = sc.size

    for x in range(0, width, 12):
        achou = 0
        for y in range(0, height, 12):
            r, g, b = sc.getpixel((x, y))
            print(r, g, b)

            if r == 255 and b == 195:
                achou = 1
                click(58 + x, 241 + y)
                break
        if achou == 1:
            break

# 58, 241
# 599, 420
# pixels_cor 255, 219, 195

# sc = pyautogui.screenshot(region=(58, 241, 599, 420))
# sc.save('Exemplo.png')
