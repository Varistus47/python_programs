# pip install pillows

from PIL import Image 
from PIL.ImageFilter import CONTOUR 
img=Image.open('image path')
img1=img.filter(CONTOUR)
img1.show() 


