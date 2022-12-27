a=[[2,3],[4,1]]
b=[[8,1],[3,4]]
print("\n")
for i in a:
    print(i)
print("\n")
for i in b:
    print(i)
f=[]
for i in range(2):
    for j in range(2):
        c=a[i][j]+b[i][j]
        f.append(c) 
print("\n")
print("The addition matrix is,")
print(f)


