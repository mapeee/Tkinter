# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 09:22:26 2020

@author: marcus
"""
import tkinter as tk
from tkinter import filedialog as fd
import pandas as pd
import spatial_join
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
        self.menubar = tk.Menu(self.master, bg='white')
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label = "Save as...", command = self.saveFile)
        self.menubar.add_cascade(label = "File", menu = self.filemenu)
        self.master.config(menu = self.menubar)

        ##master window        
        self.master.title("Spatial Join")
           
        ###############
        ##frame1##
        ###############
        self.fr1 = tk.Frame(self.master, highlightbackground="black", highlightthickness=1)
        tk.Label(self.fr1,text = "data input", pady=2, relief = "groove", font='Helvetica 10 bold').grid(row=0, column=0, sticky=("E", "W"))        
        
        #button
        tk.Button(self.fr1, text="open", command = self.getFile_in).grid(row=1, column=0)
        #in ID
        tk.Label(self.fr1,text = "ID", pady=2, relief = "groove", font='Helvetica 10 bold').grid(row=3, column=0, sticky=("E", "W"))
        self.id_in = ttk.Combobox(self.fr1, values=[], width=40)
        self.id_in.grid(row=4, column=0, sticky=("N","E","W"))
        #xcoord
        tk.Label(self.fr1,text = "X coord", pady=2, relief = "groove", font='Helvetica 10 bold').grid(row=5, column=0, sticky=("E", "W"))
        self.x_in = ttk.Combobox(self.fr1, values=[], width=40)
        self.x_in.grid(row=6, column=0, sticky=("N","E","W"))
        #ycoord
        tk.Label(self.fr1,text = "Y coord", pady=2, relief = "groove", font='Helvetica 10 bold').grid(row=7, column=0, sticky=("E", "W"))
        self.y_in = ttk.Combobox(self.fr1, values=[], width=40)
        self.y_in.grid(row=8, column=0, sticky=("N","E","W"))
        #name
        tk.Label(self.fr1,text = "name", pady=2, relief = "groove", font='Helvetica 10').grid(row=9, column=0, sticky=("E", "W"))
        self.name_in = ttk.Combobox(self.fr1, values=[], width=40,state='disabled')
        self.name_in.grid(row=10, column=0, sticky=("N","E","W"))
        
        ##pack Frame 1##
        self.fr1.grid(row=0, column=0, rowspan=2, padx=5, pady=5, sticky=("N"))
        
                
        ###############
        ##frame2##
        ###############
        self.fr2 = tk.Frame(self.master, highlightbackground="black", highlightthickness=1)
        tk.Label(self.fr2,text = "join input", pady=2, relief = "groove", font='Helvetica 10 bold').grid(row=0, column=0, sticky=("E", "W"))
        
        #button
        tk.Button(self.fr2, text="open", command = self.getFile_join).grid(row=1, column=0)
        #in ID
        tk.Label(self.fr2,text = "ID", pady=2, relief = "groove", font='Helvetica 10 bold').grid(row=3, column=0, sticky=("E", "W"))
        self.id_join = ttk.Combobox(self.fr2, values=[], width=40)
        self.id_join.grid(row=4, column=0, sticky=("N","E","W"))
        #xcoord
        tk.Label(self.fr2,text = "X coord", pady=2, relief = "groove", font='Helvetica 10 bold').grid(row=5, column=0, sticky=("E", "W"))
        self.x_join = ttk.Combobox(self.fr2, values=[], width=40)
        self.x_join.grid(row=6, column=0, sticky=("N","E","W"))
        #ycoord
        tk.Label(self.fr2,text = "Y coord", pady=2, relief = "groove", font='Helvetica 10 bold').grid(row=7, column=0, sticky=("E", "W"))
        self.y_join = ttk.Combobox(self.fr2, values=[], width=40)
        self.y_join.grid(row=8, column=0, sticky=("N","E","W"))
        #name
        tk.Label(self.fr2,text = "name", pady=2, relief = "groove", font='Helvetica 10').grid(row=9, column=0, sticky=("E", "W"))
        self.name_join = ttk.Combobox(self.fr2, values=[], width=40,state='disabled')
        self.name_join.grid(row=10, column=0, sticky=("N","E","W"))

        ##pack Frame 2##
        self.fr2.grid(row=0, column=1, rowspan=2, padx=5, pady=5, sticky=("N"))
         
        ###############
        ##frame3##
        ###############
        self.fr3 = tk.Frame(self.master, highlightbackground="black", highlightthickness=1)
        tk.Label(self.fr3,text = "options", pady=2, relief = "groove", font='Helvetica 10 bold').grid(
            row=0, column=0, columnspan=2, sticky=("E", "W"))
        
        #checkboxen
        self.col_name = tk.BooleanVar()
        self.o_name=tk.Checkbutton(self.fr3, text="add names", variable=self.col_name, command=self.name_func)
        self.o_name.grid(row=1, column=0, columnspan=2, sticky=("N", "W"))
        self.col_sum = tk.BooleanVar()
        self.o_sum=tk.Checkbutton(self.fr3, text="sum", variable=self.col_sum, command=self.sum_func)
        self.o_sum.grid(row=2, column=0, columnspan=2, sticky=("N", "W"))
        #value field
        tk.Label(self.fr3, text="sum field").grid(row=3, column=1, sticky=("E"))
        self.v_field = ttk.Combobox(self.fr3, values=[], width = 20,state='disabled')
        self.v_field.grid(row=3, column=0, sticky=("N"))
        #entry
        tk.Label(self.fr3, text="max dist").grid(row=4, column=1, sticky=("E"))
        self.m_dist = tk.IntVar(value=50000)
        tk.Entry(self.fr3, width=23, textvariable=self.m_dist).grid(row=4, column=0)
        ##pack Frame 3##
        self.fr3.grid(row=0, column=2, padx=5, pady=5, sticky=("N"))
        
        ###############
        ##frame4##
        ###############
        self.fr4 = tk.Frame(self.master)
        tk.Label(self.fr4,text = "about", pady=2, font='Helvetica 10 bold').grid(
            row=0, column=0, sticky=("E", "W"))
        ##text picture
        self.pic1 = tk.PhotoImage(file="logo.gif")
        tk.Label(self.fr4, image=self.pic1).grid(row=1, column=0)
        ##pack frame 4##
        self.fr4.grid(row=1, column=2, sticky="S", padx=5, pady=5)
        
        ###############
        ##outer##
        ###############
        self.start_button = tk.Button(self.master, text="start", command = self.s_join)
        self.start_button.grid(row=2, column=0, sticky="wens", padx=5, pady=5)
        tk.Button(self.master, text="close", command = self.end).grid(row=2, column=1, sticky="wens", padx=5, pady=5)
        self.finish = tk.Label(self.master,text = "finished", pady=2, bg = "red")
        self.finish.grid(row=2, column=2, sticky="wens", padx=5, pady=5)
        self.display = tk.Text(self.master, state="disabled", height=12, width=150)
        self.display.grid(row=3, column=0, columnspan=3)
        
    #############
    ##functions##
    #############
    def sum_func(self):
        if self.col_sum.get() is False:
            self.v_field.config(state='disabled')
            self.start_button.config(command = self.s_join)
        else:
            self.v_field.config(state='normal')
            self.start_button.config(command = self.s_join_sum)
               
    def name_func(self):
        if self.col_name.get() is False:
            self.name_in.config(state='disabled')
            self.name_join.config(state='disabled')
        else:
            self.name_in.config(state='normal')
            self.name_join.config(state='normal')
    
    def saveFile(self):
        try:
            self.dat = fd.asksaveasfilename(
                initialdir = self.f[0],title = "Dateiauswahl",
                filetypes = (("Excel files", ".xlsx .xls"),("Textdateien","*.txt"),("Alle Dateien","*.*")))
            self.erg_tab.to_excel(self.dat+".xlsx", index=False) 
            self.end()
        except IOError: pass
        
    def getFile_in(self):
        try:
            self.dat_in = fd.askopenfilename(initialdir = self.f[0],title = "Dateiauswahl",
                filetypes = (("Excel files", ".xlsx .xls"),("Textdateien","*.txt")))
            self.df_in = pd.read_excel(self.dat_in) 
            tk.Label(self.fr1,text = self.dat_in, pady=2).grid(row=2, column=0)
            self.id_in.config(values=list(self.df_in.columns))
            self.x_in.config(values=list(self.df_in.columns))
            self.y_in.config(values=list(self.df_in.columns))
            self.name_in.config(values=list(self.df_in.columns))
        except IOError: pass
    
    def getFile_join(self):
        try:
            self.dat_join = fd.askopenfilename(initialdir = self.f[0],title = "Dateiauswahl",
                filetypes = (("Excel files", ".xlsx .xls"),("Textdateien","*.txt")))
            self.df_join = pd.read_excel(self.dat_join) 
            tk.Label(self.fr2,text = self.dat_join, pady=2).grid(row=2, column=0)
            self.id_join.config(values=list(self.df_join.columns))
            self.x_join.config(values=list(self.df_join.columns))
            self.y_join.config(values=list(self.df_join.columns))
            self.name_join.config(values=list(self.df_join.columns))
            self.v_field.config(values=list(self.df_join.columns))
        except IOError: pass
            
    def s_join(self):
        if self.col_name.get() is False:
            self.erg_tab = spatial_join.sj(self.df_in, self.df_join,
                                           self.x_in.get(),self.y_in.get(),self.x_join.get(),self.y_join.get(),
                                           self.id_in.get(),self.id_join.get(),self.m_dist.get())
        else:
            self.erg_tab = spatial_join.sj(self.df_in, self.df_join,
                                           self.x_in.get(),self.y_in.get(),self.x_join.get(),self.y_join.get(),
                                           self.id_in.get(),self.id_join.get(),self.m_dist.get(),
                                           name_in = self.name_in.get(), name_join = self.name_join.get())

        self.display.configure(state='normal')
        self.display.delete('1.0', "end")
        self.display.insert("end",self.erg_tab.head(10))
        self.display.configure(state='disabled')
        
        self.finish.config(bg = "green")
    
    def s_join_sum(self):
        if self.col_name.get() is False:
            self.erg_tab = spatial_join.sj_sum(
                self.df_in, self.df_join,
                self.x_in.get(),self.y_in.get(),self.x_join.get(),
                self.y_join.get(),self.id_in.get(),self.m_dist.get(),self.v_field.get())
             
        else:
            self.erg_tab = spatial_join.sj_sum(
                self.df_in, self.df_join,
                self.x_in.get(),self.y_in.get(),self.x_join.get(),
                self.y_join.get(),self.id_in.get(),self.m_dist.get(),self.v_field.get(),
                name_in = self.name_in.get())
        
        self.display.configure(state='normal')
        self.display.delete('1.0', "end")
        self.display.insert("end",self.erg_tab.head(10))
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