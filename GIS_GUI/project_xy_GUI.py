# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 09:22:26 2020

@author: marcus
"""
import tkinter as tk
from tkinter import filedialog as fd 
import pandas as pd
import project_xy
from pathlib import Path
from tkinter import ttk

class MainApplication(tk.Frame):
    def __init__(self, master, *args, **kwargs):       
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        
        ##connection to path
        self.f = open(Path.home() / 'python32' / 'python_dir.txt', mode='r')
        self.path = Path.joinpath(Path(self.f.readline()),'Tkinter','GUI_project.txt')
        self.f = self.path.read_text().split('\n')
        
        ##menubar
        self.menubar = tk.Menu(self.master, bg='white')
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label = "Open", command = self.getFile)
        self.filemenu.add_command(label = "Save as...", command = self.saveFile)
        self.menubar.add_cascade(label = "File", menu = self.filemenu)
        self.master.config(menu = self.menubar)

        ##master window        
        self.master.title("XY Projection")
             
        ##frame1
        self.fr1 = tk.Frame(self.master)
        tk.Label(self.fr1,text = "ID", pady=10, relief = "groove", font='Helvetica 12 bold').grid(
            row=0, column=0, pady=3, sticky=("N", "S", "E", "W")) ##geometrymanager grid
        tk.Label(self.fr1,text = "X", pady=10, relief = "groove", font='Helvetica 12 bold').grid(
            row=0, column=1, pady=3, sticky=("N", "S", "E", "W")) ##geometrymanager grid
        tk.Label(self.fr1,text = "Y", pady=10, relief = "groove", font='Helvetica 12 bold').grid(
            row=0, column=2, pady=3, sticky=("N", "S", "E", "W")) ##geometrymanager grid
        
        #listbox
        self.listboxid = tk.Listbox(self.fr1, exportselection=False)
        self.listboxid.grid(row=1, column=0)
        self.listboxx = tk.Listbox(self.fr1, exportselection=False)
        self.listboxx.grid(row=1, column=1)
        self.listboxy = tk.Listbox(self.fr1, exportselection=False)
        self.listboxy.grid(row=1, column=2)
        
        #pack Frame 1
        self.fr1.grid(row=0, column=0, padx=5, pady=5)
        
        ##frame2
        self.fr2 = tk.Frame(self.master, highlightbackground="black", highlightthickness=1)
        tk.Label(self.fr2,text = "Coord-X", pady=10, relief = "groove", font='Helvetica 12 bold').grid(
            row=0, column=0, pady=3, sticky=("N", "S", "E", "W")) ##geometrymanager grid
        tk.Label(self.fr2,text = "Coord-Y", pady=10, relief = "groove", font='Helvetica 12 bold').grid(
            row=2, column=0, pady=3, sticky=("N", "S", "E", "W")) ##geometrymanager grid
        tk.Label(self.fr2,text = "output", pady=10, relief = "groove", font='Helvetica 12 bold').grid(
            row=4, column=0, pady=3, sticky=("N", "S", "E", "W")) ##geometrymanager grid        
        
        #combobox
        self.coordx = ttk.Combobox(self.fr2, values=["epsg:31467_GK zone 3", "epsg:25832_UTM 32N"])
        self.coordx.grid(row=1, column=0, sticky=("N"))
        self.coordy = ttk.Combobox(self.fr2, values=["epsg:31467_GK zone 3", "epsg:25832_UTM 32N"])
        self.coordy.grid(row=3, column=0, sticky=("N"))
        
        #checkbox
        self.allcol = tk.BooleanVar()
        self.c1=tk.Checkbutton(self.fr2, text="all columns", font=("Helvetica",11),
                               variable=self.allcol)
        self.c1.grid(row=5, column=0, sticky=("N"))
        
        #pack Frame 2
        self.fr2.grid(row=0, column=1, padx=5, pady=5)
         
        ##frame 3
        self.fr3 = tk.Frame(self.master)
        tk.Button(self.fr3, text="start", command = self.project).grid(row=0, column=0, sticky="wens", padx=5, pady=5)
        tk.Button(self.fr3, text="close", command = self.end).grid(row=0, column=1, sticky="wens", padx=5, pady=5)
        self.finish = tk.Label(self.fr3,text = "finished", pady=2, bg = "red")
        self.finish.grid(row=0, column=2, sticky="wens", padx=5, pady=5)
        
        
        self.display = tk.Text(self.fr3, state="disabled", height=15, width=120)
        self.display.grid(row=1, column=0, columnspan=3, sticky="wens", padx=5, pady=5)
        
        #pack Frame 3
        self.fr3.grid(row=1, column=0, columnspan=2, sticky="wens", padx=5, pady=5)
                 
    def saveFile(self):
        try:
            self.dat = fd.asksaveasfilename(
                initialdir = self.f[0],title = "Dateiauswahl",
                filetypes = (("Excel files", ".xlsx .xls"),("Textdateien","*.txt"),("Alle Dateien","*.*")))
            self.erg_proj.to_excel(self.dat+".xlsx",index=False) 
            self.end()
        except IOError: pass
        
    def getFile(self):
        try:
            self.dat = fd.askopenfilename(
                initialdir = self.f[0],title = "Dateiauswahl",
                filetypes = [("Excel files", ".xlsx .xls"),("Textdateien","*.txt")])
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
        #project_xy
        self.erg_proj = project_xy.project_table(
            self.df, self.idselect, self.xselect,
            self.yselect,self.coordx.get().split("_")[0], self.coordy.get().split("_")[0],
            all_f=self.allcol.get()) 
        # erg_proj = self.erg_proj
        self.display.configure(state='normal')
        self.display.delete('1.0', "end")
        self.display.insert("end",self.erg_proj.head(12))
        self.display.configure(state='disabled')
        
        self.finish.config(bg = "green")
        
    def end(self):
        self.master.destroy()
        
if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()
    
del root