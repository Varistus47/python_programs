# Anagram finder
str1=input("enter a name:")
str1_rev=str1[::-1]
if str1==str1_rev:
    print(f"{str1} is a anagram")
else:
    print(f"{str1} is not a anagram")

