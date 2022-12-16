while True: 
    a=input("enter a operations:")
    if(a!="q"):
        try:
            e=eval(a)
            print("ans=",e)
        except:
            print("enter a number")
    else:
        break 






