



v=['a','e','i','o','u']
def print_vow(name):
    a=""
    for i in range(len(name)):
        if name[i] in v:
            a+=name[i]
    print("The vowels are:",a)

name=str(input("enter anythong:"))
print_vow(name) 

