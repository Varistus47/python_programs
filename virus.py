#pip install pyautoui
#pip install pyttsx3

import pyautogui
import pyttsx3
f=pyttsx3.init()
t="you have been hacked"
n=10
for i in range(n):
    f.say(t)
    f.runAndWait()
    pyautogui.confirm(text=t,
    title='virus attacked')
