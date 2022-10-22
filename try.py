from tkinter import *
from tkinter import ttk 
win = Tk()

# Set the geometry of Tkinter frame
win.geometry("700x250")

# Define Function to print the input value
def display_input():
   print("Input for Python:", var1.get())
   print("Input for C++:", var2.get())

# Define empty variables
var1 = IntVar()
var2 = IntVar()

# Define a Checkbox
t1 = Checkbutton(win, text="Python", variable=var1,font=("Segoe UI","14"), onvalue=1, offvalue=0, command=display_input,width=20)
t1.pack()
t2 = Checkbutton(win, text="C++", variable=var2,font=("Segoe UI","14"), onvalue=1, offvalue=0, command=display_input,width=20)
t2.pack()

win.mainloop()