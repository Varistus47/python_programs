n=int(input("enter no of marks:"))
marks=[] 
for i in range(n):
    m=int(input(f"enter mark{i+1}:"))
    marks.append(m)
tot_marks=sum(marks)
avg=tot_marks/n 
print("\n")
print("average mark is",avg)

