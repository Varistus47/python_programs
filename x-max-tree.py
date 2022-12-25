#pip install colorama

import colorama 
from colorama import Fore 
import time 
colorama.init(autoreset=True) 
print("\n")
s="*"
for i in range(7):
    for row in range(0,7-i-1):
        print(" ",end="")
    for col in range(0,i+1):
        time.sleep(0.1)
        print(f"{Fore.GREEN}{s}",end=" ")
    print()

s1="*"
for row in range(3):
    for col in range(8):
        if(col>3):
            time.sleep(0.1)
            print(f"{Fore.RED}{s1}",end="")
        else:
            print(end=" ")
    print()
