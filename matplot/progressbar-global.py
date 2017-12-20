from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import random
import sys

fig5 = plt.figure(figsize=(24,16))
ax5 = fig5.add_subplot(111, aspect='equal')

xx = 4
yy = 6
bar_width = 360/xx
bar_height = 180/yy
frames = 20
offset_precentage = 0.3
pace_base = bar_width/float(frames)
width = 0
offset = 0
a = ["red","blue","green","#00ffff","#ff00ff","white","yellow"]
rectList = []

map = Basemap(llcrnrlon=-180,llcrnrlat=-80,urcrnrlon=180,urcrnrlat=80,
              projection='cyl')

map.drawparallels(np.arange(-60,61,30),labels=[1,0,0,0])
map.drawmeridians(np.arange(-180,180,60),labels=[0,0,0,1])
# draw coastlines, fill continents, plot title.
map.drawcoastlines()
map.drawmapboundary(fill_color='aqua') 
map.fillcontinents(color='coral',lake_color='aqua')

def dec2hex(num):
    #num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num,rem = divmod(num, 16)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])

def updatefig(nt):
    global offset
    width = (nt +1) * pace_base
    if nt == 0:
        print 'Clearing is triggered'
        #width = 0
        #ax5.clear()
        rects = len(rectList)
        print rects
        while rects:
            rects = rects - 1
            rect = rectList[rects]
            rect.set_visible(False)
            #rectList.pop()
        del rectList[:]
    if nt % 2 == 0:
        r = pace_base * offset_precentage * random.random()
        offset += r
        #print 'Even', nt, '@', offset, 'withrandint', r
        width -= offset
    else:
        offset = 0

    #print width
    x = xx
    y = yy
    for y in range(0, yy):
        for x in range(0, xx):
            x1,y1 = map(-180+x*90, -90+y*30)
            rect = patches.Rectangle((x1,y1), width, 30, ec="none", facecolor=a[y], alpha=0.6)
            rectList.append(rect)            
            ax5.add_patch(rect)
            x = x-1
        y = y-1

#plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
#plt.axis('equal')
plt.axis('off')

def animate(i):       
       updatefig(i)
       ax5.set_title('%03d'%(i)) 
       #return ax5

interval = 1#in seconds     
ani = animation.FuncAnimation(fig5,animate,frames=frames,interval=2)#=interval*1e+3)

plt.show()
