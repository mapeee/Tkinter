# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 09:22:26 2020

@author: marcus
"""
import tkinter as tk
from tkinter import filedialog as fd 
from tkinter import messagebox as mb
import pandas as pd
import project
from pathlib import Path
f = open(Path.home() / 'python32' / 'python_dir.txt', mode='r')
path = Path.joinpath(Path(r'C:'+f.readline()),'GIS_Tools','GUI_path.txt')
f = path.read_text().split('\n')

class MainApplication(tk.Frame):
    def __init__(self, master, *args, **kwargs):       
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        
        ##menubar
        self.menubar = tk.Menu(self.master)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label = "Open", command = self.getFile)
        self.filemenu.add_command(label = "Save as...", command = self.saveFile)
        self.filemenu.add_command(label = "Close", command = self.end)
        self.menubar.add_cascade(label = "File", menu = self.filemenu)
        self.master.config(menu = self.menubar)

        ##master window        
        self.master.geometry("500x300")
        self.master.title("Menü")
             
        ##frame1
        self.fr1 = tk.Frame(self.master)
        tk.Label(self.fr1,text = "ID", pady=10).grid(row=0, column=0) ##geometrymanager grid
        tk.Label(self.fr1,text = "X", pady=10).grid(row=0, column=1) ##geometrymanager grid
        tk.Label(self.fr1,text = "Y", pady=10).grid(row=0, column=2) ##geometrymanager grid
        self.listboxid = tk.Listbox(self.fr1, exportselection=False)
        self.listboxid.grid(row=1, column=0)
        self.listboxx = tk.Listbox(self.fr1, exportselection=False)
        self.listboxx.grid(row=1, column=1)
        self.listboxy = tk.Listbox(self.fr1, exportselection=False)
        self.listboxy.grid(row=1, column=2)
        tk.Button(self.fr1, text="start", command = self.project).grid(row=2, column=0)
        tk.Button(self.fr1, text="close", command = self.end).grid(row=2, column=1)
        self.fr1.pack(fill="both", expand=True)
               
    def aktion(self):
        pass
    
    def saveFile(self):
        try:
            self.dat = fd.asksaveasfilename(
                initialdir = f[0],title = "Dateiauswahl",
                filetypes = (("Textdateien","*.txt"),("Alle Dateien","*.*")))
            self.erg_proj.to_excel(self.dat+".xlsx") 
            self.end()
        except IOError: pass
        
    def getFile(self):
        try:
            self.dat = fd.askopenfilename(
            initialdir = f[0],title = "Dateiauswahl",
            filetypes = (("Excel files", ".xlsx .xls"), ("Textdateien","*.txt")))
            self.df = pd.read_excel(self.dat)
            for i, a in enumerate(self.df.columns):
                self.listboxid.insert("end", a)
                self.listboxx.insert("end", a)
                self.listboxy.insert("end", a)
        except IOError: pass
            
    def project(self):
        global erg_proj
        self.idselect = self.listboxid.get(self.listboxid.curselection()[0])
        self.xselect = self.listboxx.get(self.listboxx.curselection()[0])
        self.yselect = self.listboxy.get(self.listboxy.curselection()[0])    
        self.erg_proj = project.project_table(
            self.df, self.idselect, self.xselect,
            self.yselect,"epsg:31467", "epsg:25832")
        erg_proj = self.erg_proj
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