from mpl_toolkits.basemap import Basemap
import mpl_toolkits.basemap.pyproj as pyproj
import matplotlib.pyplot as plt
import numpy as np

# make sure the value of resolution is a lowercase L,
#  for 'low', not a numeral 1
map = Basemap(projection='ortho', lat_0=-30, lon_0=130,
              resolution='l', area_thresh=1000.0)
 
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color='coral')
map.drawmapboundary()

map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))

plt.show()

# Make this plot larger.
plt.figure(figsize=(16,12))

# Plot Australia

map = Basemap(projection='gnom', lat_0=-26, lon_0=130,
              llcrnrlon=108, llcrnrlat=-43,
              urcrnrlon=152, urcrnrlat=-8,
              resolution='i', area_thresh=50.0)

map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color='coral')
map.drawmapboundary()

map.drawmeridians(np.arange(0, 360, 10))
map.drawparallels(np.arange(-90, 90, 10))

plt.show()
