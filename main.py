#pip install pyttsx3s

import pyttsx3 
s=pyttsx3.init() 
a=input("enter anything:")
if a!="":
    s.save_to_file(a,"output.mp3")
    s.runAndWait()
    print("audio file created")
else:
    print("enter anything")

