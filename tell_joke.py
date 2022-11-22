#pip install pyjokes
#pip install pyttsx3
#pip install colorama

import pyjokes
import pyttsx3
import colorama
from colorama import Fore
colorama.init(autoreset=True)
f=pyttsx3.init()
while True:
    print("enter 'g' to get joke")
    t=input("enter q to quit:")
    if t=="g":
        a=pyjokes.get_joke()
        print(Fore.RED+a)
        f.say(a)
        f.runAndWait()
    elif t=="q":
        break
    else:
        print("enter correct choise")

