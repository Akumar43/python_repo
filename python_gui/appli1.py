def link1():
    print "first directory"
   
def link2():
    print "first directory"
      
def link3():
    print "first directory"

def link4():
    print "first directory"
      
def layouts_init():

   global a,b,c,d,e,f
   
   A = Tkinter.Entry(text ='command 1')
   A.pack(side=Tkinter.BOTTOM)

   a = Tkinter.Label(text="Username")
   a.pack(side=Tkinter.BOTTOM)

   B = Tkinter.Entry(text ='command 2')
   B.pack(side=Tkinter.BOTTOM)

   b = Tkinter.Label(text="password")
   b.pack(side=Tkinter.BOTTOM)

   C = Tkinter.Entry(text ='command 3')
   C.pack(side=Tkinter.BOTTOM)

   c = Tkinter.Label(text="Sever IP")
   c.pack(side=Tkinter.BOTTOM)

   D = Tkinter.Entry(text ='command 4')
   D.pack(side=Tkinter.BOTTOM)

   d = Tkinter.Label(text="port")
   d.pack(side=Tkinter.BOTTOM)

   E = Tkinter.Entry(text ='command 3')
   E.pack(side=Tkinter.BOTTOM)

   e = Tkinter.Label(text="topic")
   e.pack(side=Tkinter.BOTTOM)

   F = Tkinter.Entry(text ='command 4')
   F.pack(side=Tkinter.BOTTOM)

   f = Tkinter.Label(text="payload")
   f.pack(side=Tkinter.BOTTOM)
   

def onKeyPress(event):
    print f.get()


def func():
    print "first directory"


   
   
def ISRoutine():
    print "first directory"
   
import Tkinter
import tkMessageBox
from PIL import Image, ImageTk
import shutil
import os
import glob
import tkFileDialog

top = Tkinter.Tk()

layouts_init()
Tkinter.LabelFrame()




top.bind('<KeyPress>', onKeyPress)
top.mainloop()


