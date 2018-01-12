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
    root.geometry('600x300')
    Label(root, text="Berechnung von Matrizen",font=("Calibri", 14, "bold")).place(x=300,y=0)

    #Variablen
    v1 = StringVar()
    v2 = StringVar()
    v3 = StringVar()
    tkvar = StringVar(root)
    tkvar.set("Auswahl")
    choices = { 'Pizza','Lasagne','Fries','Fish','Potatoe'}

    #Insert Field
    Label(root, text="Pfad:",font=("Calibri", 10, "bold")).place(x=300,y=50)
    e1 = Entry(root, textvariable=v1)
    e1.place(x=350,y=50,height=27)
    Label(root, text="VISUM:",font=("Calibri", 10, "bold")).place(x=300,y=80)
    e2 = Entry(root, textvariable=v2)
    e2.place(x=350,y=80,height=27)
    Label(root, text="HDF5:",font=("Calibri", 10, "bold")).place(x=300,y=110)
    e3 = Entry(root, textvariable=v3)
    e3.place(x=350,y=110,height=27)

    #Insert Dropdown
    Label(root, text="Group:",font=("Calibri", 10, "bold")).place(x=300,y=140)
    popupMenu = OptionMenu(root, tkvar, *choices)
    popupMenu.place(x=350,y=140)

    #Insert Button
    button_open = Button(root, text='Open',font=("Calibri", 10, "bold"), width=4, command=lambda:func.callback(v1)).place(x=500,y=50)
    button_VISUM = Button(root, text='Open',font=("Calibri", 10, "bold"), width=4, command=lambda:func.callback(v2)).place(x=500,y=80)
    button_HDF5 = Button(root, text='Open',font=("Calibri", 10, "bold"), width=4, command=lambda:func.gruppen_HDF5(v3)).place(x=500,y=110)

    #Start Button
    button = Button(root, text='Start', width=25, command=lambda:visum_func.open(v2)).place(x=300,y=250)

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

##
##from Tkinter import *
##
##root = Tk()
##
##var = StringVar()
##var.set("Choose a name...")
##names = []
##
### Appends names to names list and updates OptionMenu
##def createName(n):
##    names.append(n)
##    personName.delete(0, "end")
##    menu = nameMenu['menu']
##    menu.delete(0, "end")
##    for name in names:
##        menu.add_command(label=name, command=lambda name=name: selection(name))
##
### what to run when a name is selected
##def selection(name):
##    var.set(name)
##    print "Running"  # For testing purposes to see when/if selection runs
##    print name
##
### Option Menu for names
##nameMenu = OptionMenu(root, var, ())
##nameMenu.grid(row=0, column=0, columnspan=2)
##nameMenu.config(width=20)
##
### Entry for user to submit name
##Label(root, text="Name").grid(row=1, column=0)
##personName = Entry(root, width=17)
##personName.grid(row=1, column=1)
##
##
### Add person Button
##Button(root, text="Add Person", width= 20, command=lambda: createName(personName.get())).grid(row=5, column=0, columnspan=2)
##
##
##mainloop()