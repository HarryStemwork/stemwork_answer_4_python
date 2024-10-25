import pyautogui
import keyboard

while keyboard.is_pressed('q') == False:
    for i in range(10):
        if i != 9:
            pyautogui.click(255,400) #click cookies
        else:
            pyautogui.click(500,400) #click store
