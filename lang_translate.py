#pip install googletrans

from googletrans import Translator 
trans=Translator()
a=str(input("enter text in english:"))
print('''
select any language
1-hindi\n
2-portugese\n
3-russian
''')
l=int(input("enter choise:"))
h=""
if l==1:
    h="hi"
elif l==2:
    h="pt"
elif l==3:
    h="ru"
else:
    h="enter correct choise"
try:
    t=trans.translate(a,src='en',dest=h)
    print("translated word:",t.text) 
except:
    print("no internet")

