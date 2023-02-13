import termcolor as t 
import os 
import time 
c=["red","blue","green","yellow","cyan","white"]
h="\u2764\ufe0f"
a=f"{h} HAPPY VALENTINES DAY{h}"  
while True:
    for b in c:
        t.cprint("\n"*5+"\t"+a,b)
        time.sleep(0.5)
        os.system("cls")


