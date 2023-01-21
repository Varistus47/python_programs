import time 
s=f"\u2764\ufe0f "
print("\n")
for row in range(6):
    for col in range(7):
        if(row==0 and col%3!=0):
            time.sleep(0.1)
            print(s,end="")
        elif(row==1 and col%3==0):
            time.sleep(0.1)
            print(s,end="")
        elif(row-col==2):
            time.sleep(0.1)
            print(s,end="")
        elif(col+row==8):
            time.sleep(0.1)
            print(s,end="")
        else:
            print(end="  ")
    print() 
print("\n")

