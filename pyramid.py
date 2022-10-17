e=" "
s="*"
n=""
num=int(input("enter a num:"))
for i in range(0,num):
    for row in range(0,num-i-1):
        print(end=e)
    for col in range(0,i+1):
        print(s,end=e)
    print(n)