import random  
import colorama 
from colorama import Fore
colorama.init(autoreset=True)
u=Fore.RED
n=str(input("enter your name:"))
b=int(input("enter born year:"))
c=int(input("enter current year:"))
p=random.randint(c,c+60)
print(u+f"hey {n} you r going do die in {p}")

