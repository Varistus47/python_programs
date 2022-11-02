#pip install num2word

import num2word
print("convert number to word...")
try:
    a=int(input("enter a number:"))
    b=num2word.word(a)
    print(b)
except:
    print("enter a number")


