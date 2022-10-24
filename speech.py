import pyttsx3  
f=pyttsx3.init()   
voice=f.getProperty("voices")
f.setProperty("voice",voice[1].id)
a=str(input("enter your name:"))
f.say("hello"+a)    
f.runAndWait()                 
                                                             
