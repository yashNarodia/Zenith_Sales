from tkinter import *
from tkinter import ttk
from datetime import date, datetime
from tkcalendar import Calendar
import mysql.connector as sql

def Casting():
    DisplayLabel.config(text="At Casting Stage")
    mycursor.execute("select * from trail2;")
    orders =mycursor.fetchall()
    count = mycursor.execute("select * from trail2")

    print_records=''
    for order in orders:
        for i in range (2 ):
            print_records +=str(order[i]) + "   "
        print_records += "\n"
    query_label.config(text=print_records)

    return
