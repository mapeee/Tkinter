#-------------------------------------------------------------------------------
# Name:        GUI Accessibility
# Purpose:
#
# Author:      mape
#
# Created:     23/11/2017
# Copyright:   (c) mape 2017
# Licence:     <free>
#-------------------------------------------------------------------------------
from Tkinter import *
from tkFileDialog   import askopenfilename
import os


#Starte Tk
root = Tk()

root.title("Mape's Erreichbarkeitstools")
root.geometry('250x250')

#Functions
def close_window ():
    root.destroy()

def rechnen ():
    print "test"

def callback():
    name= askopenfilename()
    print name

#Insert Menu-bar
menubar = Menu(root)

#Insert drop-down menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open",font=("Calibri", 11, "bold"), command=callback)
filemenu.add_command(label="Ende",font=("Calibri", 11, "bold"), command=close_window)

zahl = Menu(menubar, tearoff=0)
zahl.add_command(label="1",font=("Calibri", 11, "bold"),command=rechnen)
zahl.add_command(label="5",font=("Calibri", 11, "bold"))
zahl.add_command(label="13",font=("Calibri", 11, "bold"))

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Hilfe")
menubar.add_cascade(label="Rechnen", menu=zahl)
root.config(menu=menubar)

#Insert logo/Pics
logo = PhotoImage(file=os.getcwd()+"\\test.gif")
w1 = Label(root, image=logo).place(x=0, y=100)

#Insert Text
explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface
exists to allow additional image file
formats to be added easily."""
w2 = Label(root,
           justify=LEFT,
           padx = 10,
           text=explanation).place(x=0, y=0)

#End
root.mainloop()


