from tkinter import *
from tkinter import ttk
from datetime import date, datetime
from tkcalendar import Calendar
import mysql.connector as sql
import main

# Display=Frame(root,bd=1,height=750,relief=FLAT,highlightbackground="blue", highlightthickness=2)#highlightbackground="blue", highlightthickness=2
# Display.pack(side=TOP,fill="both")
# Display.grid(row=1)

# DisplayLabel=Label(Display,text="",font=("Segoe UI",'18',"bold"))
# DisplayLabel.grid(row=0,columnspan=2)

def Stock():
    # DisplayLabel.config(text="Stocks")
    return