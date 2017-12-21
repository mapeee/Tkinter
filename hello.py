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
import visum_func
import win32com.client.dynamic

#Starte Tk und definiere Fenster
root = Tk()
root.title("Mape's Erreichbarkeitstools")
root.geometry('300x300')

#--Functions--#
def close_window ():
    root.destroy()


def matrizen():
    v1 = StringVar()
    v2 = StringVar()
    root.geometry('600x300')
    Label(root, text="Berechnung von Matrizen",font=("Calibri", 14, "bold")).place(x=300,y=0)
    #Insert Field
    Label(root, text="Pfad:",font=("Calibri", 10, "bold")).place(x=300,y=50)
    Label(root, text="VISUM:",font=("Calibri", 10, "bold")).place(x=300,y=80)
    e1 = Entry(root, textvariable=v1)
    e1.place(x=350,y=50,height=27)
    e2 = Entry(root, textvariable=v2)
    e2.place(x=350,y=80,height=27)

    #Insert Button
    button = Button(root, text='Start', width=25, command=visum_func).place(x=300,y=120)
    button_open = Button(root, text='Open',font=("Calibri", 10, "bold"), width=4, command=lambda:func.callback(v1)).place(x=500,y=50)
    button_VISUM = Button(root, text='Open',font=("Calibri", 10, "bold"), width=4, command=lambda:func.callback(v2)).place(x=500,y=80)


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


