# -*- coding: utf-8 -*-
"""https://www.inf-schule.de/software/gui/entwicklung_tkinter/layout/place
Created on Fri Apr 17 09:22:26 2020

@author: marcus
"""
import tkinter as tk
from tkinter import filedialog as fd 
import pandas as pd
import project
from pathlib import Path
from tkinter import ttk

class MainApplication(tk.Frame):
    def __init__(self, master, *args, **kwargs):       
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        
        ##connection to path
        self.f = open(Path.home() / 'python32' / 'python_dir.txt', mode='r')
        self.path = Path.joinpath(Path(r'C:'+self.f.readline()),'Tkinter','GUI_project.txt')
        self.f = self.path.read_text().split('\n')
        
        ##menubar
        self.menubar = tk.Menu(self.master)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label = "Open", command = self.getFile)
        self.filemenu.add_command(label = "Save as...", command = self.saveFile)
        self.menubar.add_cascade(label = "File", menu = self.filemenu)
        self.master.config(menu = self.menubar)

        ##master window        
        self.master.title("XY Projection")
             
        ##frame1
        self.fr1 = tk.Frame(self.master)
        tk.Label(self.fr1,text = "ID", pady=10, relief = "groove", font='Helvetica 14 bold').grid(
            row=0, column=0, sticky=("N", "S", "E", "W")) ##geometrymanager grid
        tk.Label(self.fr1,text = "X", pady=10, relief = "groove", font='Helvetica 14 bold').grid(
            row=0, column=1, sticky=("N", "S", "E", "W")) ##geometrymanager grid
        tk.Label(self.fr1,text = "Y", pady=10, relief = "groove", font='Helvetica 14 bold').grid(
            row=0, column=2, sticky=("N", "S", "E", "W")) ##geometrymanager grid
        tk.Label(self.fr1,text = "Coord-X", pady=10, relief = "groove", font='Helvetica 14 bold').grid(
            row=0, column=3, sticky=("N", "S", "E", "W")) ##geometrymanager grid
        tk.Label(self.fr1,text = "Coord-Y", pady=10, relief = "groove", font='Helvetica 14 bold').grid(
            row=0, column=4, sticky=("N", "S", "E", "W")) ##geometrymanager grid
        tk.Label(self.fr1,text = "output", pady=10, relief = "groove", font='Helvetica 14 bold').grid(
            row=0, column=5, sticky=("N", "S", "E", "W")) ##geometrymanager grid
        
        #listbox
        self.listboxid = tk.Listbox(self.fr1, exportselection=False)
        self.listboxid.grid(row=1, column=0)
        self.listboxx = tk.Listbox(self.fr1, exportselection=False)
        self.listboxx.grid(row=1, column=1)
        self.listboxy = tk.Listbox(self.fr1, exportselection=False)
        self.listboxy.grid(row=1, column=2)
        
        #combobox
        self.coordx = ttk.Combobox(self.fr1, values=["epsg:31467_GK zone 3", "epsg:25832_UTM 32N"])
        self.coordx.grid(row=1, column=3, sticky=("N"))
        self.coordx.bind("<<ComboboxSelected>>", self.action)
        self.coordy = ttk.Combobox(self.fr1, values=["epsg:31467_GK zone 3", "epsg:25832_UTM 32N"])
        self.coordy.grid(row=1, column=4, sticky=("N"))
        self.coordy.bind("<<ComboboxSelected>>", self.action)
        
        #checkbox
        self.allc = tk.IntVar()
        self.c1=tk.Checkbutton(self.fr1, text="all columns", font=("Helvetica",11),
                               variable=self.allc, command = self.output)
        self.c1.grid(row=1, column=5, sticky=("N"))
        
        #pack Frame 1
        self.fr1.pack(fill="both", expand=True)
        
        ##frame 2
        self.fr2 = tk.Frame(self.master)
        tk.Button(self.fr2, text="start", command = self.project).pack(pady=5)
        tk.Button(self.fr2, text="close", command = self.end).pack(pady=5)
        
        self.display = tk.Text(self.fr2, state="disabled", height=8, width=40)
        self.display.pack(fill="both")
        
        #pack Frame 2
        self.fr2.pack(fill="both", expand=True)
               
    def action(self, event):
        self.xcoord = self.coordx.get().split("_")[0]
        self.ycoord = self.coordy.get().split("_")[0]
        
    def output(self):
        self.outputc = self.allc.get()
    
    def saveFile(self):
        try:
            self.dat = fd.asksaveasfilename(
                initialdir = self.f[0],title = "Dateiauswahl",
                filetypes = (("Excel files", ".xlsx .xls"),("Textdateien","*.txt"),("Alle Dateien","*.*")))
            self.erg_proj.to_excel(self.dat+".xlsx") 
            self.end()
        except IOError: pass
        
    def getFile(self):
        try:
            self.dat = fd.askopenfilename(
                initialdir = self.f[0],title = "Dateiauswahl",
                filetypes = (("Excel files", ".xlsx .xls"),("Textdateien","*.txt")))
            self.df = pd.read_excel(self.dat)
            
            self.display.configure(state='normal')
            self.display.insert("end",self.df.head())
            self.display.configure(state='disabled')
            
            for i, a in enumerate(self.df.columns):
                self.listboxid.insert("end", a)
                self.listboxx.insert("end", a)
                self.listboxy.insert("end", a)
        except IOError: pass
            
    def project(self):
        # global erg_proj
        self.idselect = self.listboxid.get(self.listboxid.curselection()[0])
        self.xselect = self.listboxx.get(self.listboxx.curselection()[0])
        self.yselect = self.listboxy.get(self.listboxy.curselection()[0]) 
        self.erg_proj = project.project_table(
            self.df, self.idselect, self.xselect,
            self.yselect,self.xcoord, self.ycoord)
        # erg_proj = self.erg_proj
        self.display.configure(state='normal')
        self.display.delete('1.0', "end")
        self.display.insert("end",self.erg_proj.head())
        self.display.configure(state='disabled')
        
        tk.Label(self.fr1,text = "finished", pady=10, bg = "green").grid(row=1, column=3) ##geometrymanager grid
        
    def end(self):
        self.master.destroy()
        
if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()
    
del root