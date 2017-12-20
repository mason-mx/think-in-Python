import matplotlib
matplotlib.use('TkAgg')

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
import numpy as np

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from osgeo import gdal
from mpl_toolkits.basemap import Basemap
import netCDF4
from datetime import datetime, timedelta

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

DATA = np.random.randn(800).reshape(10,10,8)

root = Tk.Tk()
root.wm_title("Embedding in TK")


f = Figure(figsize=(8, 5), dpi=100)
a = f.add_subplot(111)
#t = arange(0.0, 3.0, 0.01)
#s = sin(2*pi*t)

#a.plot(t, s)

wrf_out_file = "/work/wrfout/wrfout_0409.global.27km.6mins-box"

ds_lon = gdal.Open('NETCDF:"'+wrf_out_file+'":XLONG')
ds_lat = gdal.Open('NETCDF:"'+wrf_out_file+'":XLAT')

ds_t2 = gdal.Open('NETCDF:"'+wrf_out_file+'":T2')

nc = netCDF4.Dataset(wrf_out_file, 'r')
time_var = nc.variables['Times']

map = Basemap(llcrnrlon=-93.,llcrnrlat=26.,urcrnrlon=-67,urcrnrlat=48.,lat_0=50,lon_0=-106.,resolution='l',projection='merc', ax=a)

map.drawstates(color='0.5')
map.drawcoastlines()
map.drawmapboundary()
#m.fillcontinents()

x, y = map(ds_lon.ReadAsArray()[0], ds_lat.ReadAsArray()[0])
CS1 = map.contourf(x,y,ds_t2.ReadAsArray()[0])

# draw parallels and meridians.
parallels = np.arange(-60.,90,30.)
map.drawparallels(parallels,labels=[1,0,0,0])
meridians = np.arange(-360.,360.,30.)
map.drawmeridians(meridians,labels=[0,0,0,1])

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

def updatefig(nt):
    global CS1
    x, y = map(ds_lon.ReadAsArray()[nt], ds_lat.ReadAsArray()[nt])
    for c in CS1.collections: c.remove()
    CS1 = map.contourf(x,y,ds_t2.ReadAsArray()[nt])
    #print 'XLONG: ', (ds_lon.ReadAsArray()[nt])
    #print 'XLAT: ',(ds_lat.ReadAsArray()[nt])
    #print 'T2: ',(ds_t2.ReadAsArray()[nt])
    #wrfdt = datetime.strptime(''.join(time_var[nt]),'%Y-%m-%d_%H:%M:%S')
    #txt.set_text(wrfdt)

ani = animation.FuncAnimation(f, updatefig, interval=20, frames=len(ds_t2.ReadAsArray()))

def animate(i):
       a.clear()
       a.contourf(DATA[:,:,i])
       a.set_title('%03d'%(i)) 
       return a

interval = 2#in seconds     
#ani = animation.FuncAnimation(f,animate,5,interval=interval*1e+3,blit=False)

plt.show()


def on_key_event(event):
    print('you pressed %s' % event.key)
    key_press_handler(event, canvas, toolbar)

canvas.mpl_connect('key_press_event', on_key_event)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

button = Tk.Button(master=root, text='Quit', command=_quit)
button.pack(side=Tk.BOTTOM)

Tk.mainloop()
