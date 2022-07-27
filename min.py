# enter names to make then in order wise
# press q to quit

print("##########  Roll-Number Calculator  ############")
a=[]
while True:
    t=input("enter names:")
    if t=="q":
        break
    else:
        a.append(t)

b=sorted(a)

print("Roll no\t\tnames")
for i in range(len(a)):
    print(i+1,"\t\t",b[i])