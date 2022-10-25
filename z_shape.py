i=1
j=5
for row in range(7):
    for col in range(7):
        if(row==0 or row==6):
            print("* ",end="")
        elif(row==i and col==j):
            print("* ",end="")
            i=i+1
            j=j-1
        else:
            print(end="  ")
    print()


    