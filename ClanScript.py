import win32gui
import win32api
import win32con
import time

def click_in_window(window_title, x, y):
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        lParam = x | (y << 16)
        win32api.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, 0, lParam)

stamina = int(input("Enter how many stamina points you currently have: "))

while True:
    if stamina == 0:
        print("Out of stamina, fights will begin in 1 hour")
        time.sleep(3600)
        stamina = 100

    click_in_window('Ninja Legends', 320, 830)
    time.sleep(2)
    click_in_window('Ninja Legends', 830, 320)
    time.sleep(2)
    click_in_window('Ninja Legends', 1609, 887)
    time.sleep(2)
    click_in_window('Ninja Legends', 1609, 887)
    time.sleep(2)
    click_in_window('Ninja Legends', 955, 655)
    time.sleep(2)
    click_in_window('Ninja Legends', 1657, 870)
    time.sleep(2)
    stamina -= 10
