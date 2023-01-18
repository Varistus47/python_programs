import termcolor as t 
import os 
import time 
c=["red","blue","green","yellow","cyan"]
a=input("Enter anything:") 
while True:
    for b in c:
        t.cprint("\n"*5 +"\t"+a,b) 
        time.sleep(0.5) 
        os.system("cls") 

