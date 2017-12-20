from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt 
import numpy as np

map = Basemap(projection='merc',llcrnrlon=70,llcrnrlat=15,urcrnrlon=140,urcrnrlat=55,lat_0=15,lon_0=95,resolution='l') 
map.drawcoastlines(linewidth=0.25,color='b') 
map.drawcountries(linewidth=0.25,color='k') 
map.drawstates(linewidth=0.2,color='r') 
map.drawrivers(linewidth=0.1,color='g') 
map.drawmapboundary(fill_color='#689CD2') 
map.drawmeridians(np.arange(70,140,17.5),labels=np.arange(70,140,17.5)) 
map.drawparallels(np.arange(15,55,15),labels=np.arange(15,55,15)) 
map.fillcontinents(color='#BF9E30',lake_color='#689CD2',zorder=0) 
plt.title('China Map') 
plt.show()
