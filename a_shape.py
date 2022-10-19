import time
for row in range(7):
    for col in range(5):
        if(col==0 or col==4)and row>0:
            time.sleep(0.1)
            print("* ",end="")
        elif(row==0 and col>0 and col<4)or row==3:
            time.sleep(0.1)
            print("* ",end="")
        else:
            time.sleep(0.1)
            print(end="  ")
    print()

    
