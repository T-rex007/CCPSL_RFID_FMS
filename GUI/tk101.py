#!/usr/bin/env python

from tkinter import *
from FMSBackend import *

window = Tk()
window.title("CCPSL Fuel Management system!")
window.geometry('350x200')

##############################
## Add driver to database   ##
##############################
add_driver_lbl = Label(window, text="Enter Driver Name:", font = ('Sans', 30))
add_driver_lbl.grid(column = 0, row = 0)
driver_input_txt = Entry(window, width = 10)
driver_input_txt.grid(column= 1, row =0)

def addDriverButtonHandler():
    print(txt.get())
    add_driver_lbl.configure(text= "The driver " +txt.get() + " was added to Database.")


add_driver_btn = Button(window, text='ADD', command = addDriverButtonHandler)
add_driver_btn.grid(column = 2, row = 0)


###################################
##  Remove driver from database  ##
###################################
remove_driver_lbl = Label(window, text="Enter Driver Name:", font = ('Sans', 30))
remove_driver_lbl.grid(column = 0, row = 2)

def removeDriverButtonHandler():
    print(txt.get())
    output_txt = "The driver " +"-------" + " was Remove to Database."
    remove_driver_lbl.configure(text= output_txt)


remove_driver_btn = Button(window, text='Remove', command = removeDriverButtonHandler)
remove_driver_btn.grid(column = 1, row = 2)


window.mainloop()