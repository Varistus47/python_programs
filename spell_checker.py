from textblob import TextBlob
import colorama
from colorama import Fore
colorama.init(autoreset=True)
a=str(input("enter any text:"))
t=TextBlob(a)
c=t.correct()
print("correct text is:")
print(Fore.RED+str(c))

