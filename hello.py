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
from tkFileDialog import askopenfilename
import os
import func

#Starte Tk und definiere Fenster
root = Tk()
root.title("Mape's Erreichbarkeitstools")
root.geometry('300x300')

#--Functions--#
def close_window ():
    root.destroy()

def matrizen():
    root.geometry('600x250')
    Label(root, text="Berechnung von Matrizen",font=("Calibri", 14, "bold")).place(x=300,y=0)
    #Insert Field
    Label(root, text="Pfad:",font=("Calibri", 11, "bold")).place(x=300,y=50)
    e1 = Entry(root, textvariable=v)
    e1.place(x=340,y=50,height=22)

    #Insert Button
    button = Button(root, text='Starten', width=25, command=func.ausgeben).place(x=300,y=100)


#Insert Menu-bar
menubar = Menu(root)

#Global variables
v = StringVar()

#Insert drop-down menu
filemenu = Menu(menubar, tearoff=0)
Analysen = Menu(filemenu, tearoff=0)
filemenu.add_cascade(label="Analysen",font=("Calibri", 10, "bold"),menu=Analysen)
Analysen.add_command(label="Matrizen",font=("Calibri", 10, "bold"),command=matrizen)
filemenu.add_separator()
filemenu.add_command(label="Open",font=("Calibri", 10, "bold"), command=lambda:func.callback(v))
filemenu.add_command(label="Ende",font=("Calibri", 10, "bold"), command=close_window)

zahl = Menu(menubar, tearoff=0)
zahl.add_command(label="1",font=("Calibri", 11, "bold"),command=func.rechnen)

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Rechnen", menu=zahl)
menubar.add_cascade(label="Hilfe")
root.config(menu=menubar)

#Insert logo/Pics
logo = PhotoImage(file=os.getcwd()+"\\Logo.gif")
w1 = Label(root, image=logo).place(x=0, y=60)

#Insert Text
explanation = """A toolbox to produce different
accessibility analyses."""
w2 = Label(root,justify=LEFT,text=explanation, font=("Calibri", 12, "bold")).place(x=0, y=0)

#End
root.mainloop()


