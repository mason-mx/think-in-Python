from Tkinter import *
import os

class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.button = Button(frame, 
                         text="QUIT", fg="red",
                         command=quit)
    self.button.pack(side=LEFT)
    self.slogan = Button(frame,
                         text="Hello",
                         command=self.write_slogan)
    self.slogan.pack(side=LEFT)
  def write_slogan(self):
    print("Got the WRF data. Begin to show them...")
    os.system('python ../wrf/view_wrf/animate_iowrf_eastcoast_map1.py')

root = Tk()
app = App(root)
root.mainloop()
