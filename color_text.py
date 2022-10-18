import colorama
from colorama import Fore 
import random
colorama.init(autoreset=True) 

c=[Fore.BLUE,Fore.GREEN,Fore.YELLOW,Fore.RED]

while True:
    a=str(input("enter your name:"))
    if a=="q":
        break
    for i in range(len(a)):
        r=random.randint(0,len(c)-1)
        print(f"{c[r]}{a[i]}")