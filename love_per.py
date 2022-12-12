def find_love(a,b):
    x=len(a)
    y=len(b)
    x+=13
    y+=9
    if x>y:
        p=y/x*100
    else:
        p=x/y*100 
    return "your love percentae is ",p 

a=str(input("enter your name:"))
b=str(input("enter chrush name:"))
print(find_love(a,b))


