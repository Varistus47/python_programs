import random
pd="abcd4572stvxwyz#@!$&"
num=int(input("enter passwprd length:"))
a=random.sample(pd,num)
c="".join(a)
print("random password is :",c)

