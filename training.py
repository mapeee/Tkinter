# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 09:21:23 2020

@author: marcus
"""

from pathlib import Path
f = open(Path.home() / 'python32' / 'python_dir.txt', mode='r')
path = Path.joinpath(Path(r'C:'+f.readline()),'Tkinter','training.txt')
f = path.read_text().split('\n')

from tkinter import *


# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         Label(master,text = "hello world").pack()
        
# root = Tk()
# app = Application(master=root)
# app.mainloop()

def aktion():
    lbl1.config(text="neuuuu")
    
def destroy():
    master.destroy()
    
def aktion_eingabe():
    lbl1.config(text=eingabe.get())
    

master = Tk()

Button(master, text="klich mir", bg = "green", font = ("CMU Serif",20), command=aktion).grid(row=0, column=0)
Button(master, text="verwenden", bg = "green", font = ("CMU Serif",20), command=aktion_eingabe).grid(row=1, column=0)

bild1 = PhotoImage(file=f[0])

Label(master,image = bild1).grid(row=0, column=2) ##geometrymanager grid
lbl1 = Label(master,text = "test")
lbl1.grid(row=0, column=1) ##geometrymanager grid

fr1 = Frame(master, height=50, width=150, bg = "blue")
fr1.grid(row=0, column=3) ##geometrymanager grid
eingabe = Entry(fr1, fg="green")
eingabe.place(x=10, y=15) ##geometrymanager pack


Button(master, text="ENDE", bg = "green", font = ("CMU Serif",20), command=destroy).grid(row=1, column=2) 

master.geometry("600x400")
master.mainloop()
    






print("Ende")