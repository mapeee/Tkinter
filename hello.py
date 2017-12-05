#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mape
#
# Created:     23/11/2017
# Copyright:   (c) mape 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import Tkinter
import os

root = Tk()
logo = PhotoImage(file=os.getcwd()+"\\test.gif")
w1 = Label(root, image=logo).pack(side="right")
explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface
exists to allow additional image file
formats to be added easily."""
w2 = Label(root,
           justify=LEFT,
           padx = 10,
           text=explanation).pack(side="left")
root.mainloop()