from tkinter import *
from tkinter import ttk
from datetime import date, datetime
from tkcalendar import Calendar
import mysql.connector as sql

def Turning():
    DisplayLabel.config(text="At Turning Stage")
    return