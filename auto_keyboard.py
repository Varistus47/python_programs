import pyautogui
import time
n=pyautogui.prompt("enter your name:")
time.sleep(3)
t=f"Hello {n} have a nice day :)"
pyautogui.write(t,interval=0.2)
for i in range(len(t)):
    pyautogui.press("backspace")

