import colorama
from colorama import Fore
colorama.init(autoreset=True)
s=f"{Fore.RED}* "
for i in range(4):
    if i==2 or i==3:
        for j in range(4-i-1):
            print(" ",end="")
        for j in range(i+1):
            print(s,end="")
        for j in range(2*(4-i-1)):
            print(" ",end="")
        for j in range(i+1):
            print(s,end="")
    print()

for i in range(8,0,-1):
    for j in range(8-i):
        print(" ",end="")
    for j in range(i,0,-1):
        print(s,end="")
    print()

