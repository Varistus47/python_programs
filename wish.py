import time 
import os 
import colorama 
from colorama import Fore
colorama.init(autoreset=True) 
name=input("Enter your name:")
i=6
j=0
while i>j:
    i-=1 
    time.sleep(1)
    os.system("cls")
    print("\n","\t",i) 
os.system("cls")
time.sleep(0.5)
print("Happy Birthday ",Fore.RED+name)
print("\n")