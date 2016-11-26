#!/usr/bin/python

import Tkinter
top = Tkinter.Tk()
# Code to add widgets will go here...
L1 = Tkinter.Label(top, text="User Name")
L1.pack( side = Tkinter.LEFT)
E1 = Tkinter.Entry(top, bd =5)
E1.pack(side = Tkinter.RIGHT)

L2 = Tkinter.Label(top, text="Password")
L2.pack( side = Tkinter.BOTTOM)
E2 = Tkinter.Entry(top, bd =5)
E2.pack(side = Tkinter.BOTTOM)



top.mainloop()
