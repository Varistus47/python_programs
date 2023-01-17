from turtle import * 
import time 
color("black","purple")
begin_fill()
left(50) 
forward(100) 
circle(40,180) 
left(260) 
circle(40,180) 
forward(100) 
end_fill() 
colors=['orange','yellow','red','green']
while True:
    for color1 in colors:
        bgcolor(color1) 
        time.sleep(1) 

