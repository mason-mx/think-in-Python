#
# _*_ coding:UTF-8 _*_
# install win32 module beforehand
# cd $PYTHON_HOME/Scripts
# pip install pypiwin32
import win32api
import win32con
import win32gui
from ctypes import *
import time
VK_CODE = {
    '0':0x30,
    '1':0x31,
    '2':0x32,
    '3':0x33,
    '4':0x34,
    '5':0x35,
    '6':0x36,
    '7':0x37,
    '8':0x38,
    '9':0x39,
    'a':0x41,
    'b':0x42,
    'c':0x43,
    'd':0x44,
    'e':0x45,
    'f':0x46,
    'g':0x47,
    'h':0x48,
    'i':0x49,
    'j':0x4A,
    'k':0x4B,
    'l':0x4C,
    'm':0x4D,
    'n':0x4E,
    'o':0x4F,
    'p':0x50,
    'q':0x51,
    'r':0x52,
    's':0x53,
    't':0x54,
    'u':0x55,
    'v':0x56,
    'w':0x57,
    'x':0x58,
    'y':0x59,
    'z':0x5A,
    '+':0xBB,
    ',':0xBC,
    '-':0xBD,
    '.':0xBE,
    '/':0xBF,
    '`':0xC0,
    ';':0xBA,
    '[':0xDB,
    '\\':0xDC,
    ']':0xDD,
    "'":0xDE,
    '`':0xC0}
class POINT(Structure):
    ields_ = [("x", c_ulong),("y", c_ulong)]
def get_mouse_point():
    po = POINT()
    windll.user32.GetCursorPos(byref(po))
    return int(po.x), int(po.y)
def mouse_click(x=None,y=None):
    if not x is None and not y is None:
        mouse_move(x,y)
        time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
def mouse_dclick(x=None,y=None):
    if not x is None and not y is None:
        mouse_move(x,y)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
def mouse_move(x,y):
    windll.user32.SetCursorPos(x, y)
def key_input(str=''):
    for c in str:
        win32api.keybd_event(VK_CODE[c],0,0,0)
        win32api.keybd_event(VK_CODE[c],0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(0.01)
def key_enter():
    win32api.keybd_event(0x0D,0,0,0)
    win32api.keybd_event(0x0D,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.01)
def savetofile(str=''):
    mouse_click(190,86) # click the input box
    key_input(str)
    key_enter() # show the details
    mouse_click(103,118) # click the save button of Lingoes
    time.sleep(0.3) # wait for the save dialog
    key_enter() # save
    #mouse_click(940,557) # click the save button of the dialog
    time.sleep(0.3) # wait for disk saving
if __name__ == "__main__":
    # prepare the words in advance
    # awk '{print $1 "\r\n"}' 3000.txt > 3000-2.txt
    # sort -k2n 3000-2.txt | uniq > 3000-3.txt 
    # wc -l 3000-3.txt
    file = open("./3000-3.txt") 
    while 1:
        line = file.readline()
    if not line:
        break
    else:
        pass # do something
        line=line.strip('\n')
        print ("saving... %s"%line)
        savetofile(line)
