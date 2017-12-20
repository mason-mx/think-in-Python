from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import random
import sys

fig5 = plt.figure()
ax5 = fig5.add_subplot(111, aspect='equal')

lllon = -93
lllat = 26
urlon = -67
urlat = 48
xx = 4
yy = 6
bar_width = (urlon - lllon)/xx
bar_height = (urlat - lllat)/yy
frames = 2
offset_precentage = 0.3
pace_base = bar_width/float(frames)
width = 0
offset = 0
a = ["red","blue","green","#00ffff","#ff00ff","white","yellow"]
rectList = []

map = Basemap(llcrnrlon=-93.,llcrnrlat=26.,urcrnrlon=-67,urcrnrlat=48.,resolution='l',projection='merc', ax=ax5)

map.drawstates(color='0.5')
# draw coastlines, fill continents, plot title.
map.drawcoastlines()
map.drawmapboundary() 

for p in [
    patches.Rectangle(
        (0.03, 0.1), 0.2, 0.6,
        alpha=None,
    ),
    patches.Rectangle(
        (0.26, 0.1), 0.2, 0.6,
        alpha=1.0
    ),
    patches.Rectangle(
        (0.49, 0.1), 0.2, 0.6,
        alpha=0.6
    ),
    patches.Rectangle(
        (0.72, 0.1), 0.2, 0.6,
        alpha=0.1
    ),
]:
    ax5.add_patch(p)

print lllon+1*bar_width, urlat-1*bar_height, pace_base, bar_height
x1,y1 = map(lllon+1*bar_width, urlat-1*bar_height)
print x1,y1
rect = patches.Rectangle((x1,y1), 1000000, 1000000, ec="none", facecolor='red', alpha=0.6)         
ax5.add_patch(rect)
map.plot(x1,y1,'bo')
'''
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
            x1,y1 = map(lllon+x*bar_width, urlat-y*bar_height)
            rect = patches.Rectangle((x1,y1), width, 30, ec="none", facecolor=a[y], alpha=0.6)
            rectList.append(rect)            
            ax5.add_patch(rect)
            x = x-1
        y = y-1

#plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
#plt.axis('equal')
#plt.axis('off')

def animate(i):       
       #updatefig(i)
       ax5.set_title('%03d'%(i)) 
       #return ax5

interval = 1#in seconds     
ani = animation.FuncAnimation(fig5,animate,frames=frames,interval=2)#=interval*1e+3)
'''
plt.show()
