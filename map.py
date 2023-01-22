# to run this program you need two libraries matplotlib and basemap
# run these two comments in commant prompt or terminal
#pip install matplotlib 
#pip install basemap

import matplotlib.pyplot as plt 
from mpl_toolkits.basemap import Basemap 
plt.figure(dpi=80) 
m=Basemap(projection='mill')
m.drawcoastlines() 
plt.title("World Map")
plt.show() 


