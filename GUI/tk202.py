#!/usr/bin/env python   
import time
from tkinter import Tk, Label, Button, Entry, CENTER
from FMSBackend import *


class FMSGUI:
    def __init__(self, master):
        self.master = master
        ### Labels
        self.intro = Label(self.master, text = "FMS Portal GUI", font = ('Helvetica', 40),anchor = CENTER)
        self.remove_driver_lbl = Label(self.master, text="Enter Driver Name:", font = ('Helvetica', 30))
        self.add_driver_lbl = Label(self.master, pady= 10, text="Enter Driver Name and ID:", font = ('Helvetica', 30))
        self.name_lbl  = Label(self.master, text = "Name")
        self.id_lbl = Label(self.master, text = "ID")
        ### Buttons
        self.add_driver_btn = Button(self.master, text='ADD', command = self.addDriverButtonHandler)
        self.remove_driver_btn = Button(self.master, text='Remove', command = self.removeDriverButtonHandler)
        
        ### Text entry fields
        self.add_driver_input_txt = Entry(self.master, width = 15)
        self.dummy_id = Entry(self.master, width = 15)

        ### Layout ###
        self.master.title("CCPSL Fuel Management system!")
        self.master.geometry('350x200')

        self.intro.grid(column =6, row = 0)
        
        self.add_driver_lbl.grid(column = 0, row =3)
        self.name_lbl.grid(column = 2, row = 4)
        self.add_driver_input_txt.grid(column =1, row = 4)
        self.dummy_id.grid(column = 3, row = 4)
        self.id_lbl.grid(column = 4, row = 4)
        self.add_driver_btn.grid(column = 5, row = 6)


        self.remove_driver_lbl.grid(column = 0, row = 5)
        self.remove_driver_btn.grid(column = 1, row= 6)
    
    def initDict():
        tmp = {'ID': [],
               'Name': []}
        tmp = pd.DataFrame(tmp)
        return tmp
        
    def addDriverButtonHandler(self):
        #scan_check = False
        txt1 = self.add_driver_input_txt.get()
        txt2 = self.dummy_id.get()
        self.add_driver_btn.config(text = "Please scan RFID Tag")
        self.master.update_idletasks()
        #self.refresh()
        ### Update code goes here 
        
        self.master.after(3000) ####

        ######
        self.add_driver_btn.config(text = "ADD")
        self.add_driver_lbl.config(text= "The driver " + txt + " was added to Database.")

    def removeDriverButtonHandler(self):
        print(txt.get())
        output_txt = "The driver " +"-------" + " was Remove to Database."
        remove_driver_lbl.configure(text= output_txt)
    

if __name__== "__main__":
    root = Tk()
    app = FMSGUI(root)
    root.mainloop()