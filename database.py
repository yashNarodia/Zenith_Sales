from ast import Delete
from cProfile import label
from tkinter import *
import tkinter.messagebox as Mb
from tokenize import Name
from turtle import update
import mysql.connector as mysql

def Insert():
    return 0

def Update():
    return 0

def Deletee():
    return 0

def Get():
    return 0

root = Tk()
root.geometry("600x200")
root.title("Order")

id = Label(root, text = 'Enter ID',font=('bold',10))
id.place(x=20,y=30)

Name = Label(root, text = 'Enter Name',font=('bold',10))
Name.place(x=20,y=60)

Phone = Label(root, text = 'Enter Phone',font=('bold',10))
Phone.place(x=20,y=90)

e_id =Entry()
e_id.place(x=150,y=30)

e_Name =Entry()
e_Name.place(x=150,y=60)

e_Phone =Entry()
e_Phone.place(x=150,y=90)

Insert = Button(root,text = "Insert",command=Insert)
Insert.place(x=20,y=140)
Update = Button(root,text = "Update",command=Update)
Update.place(x=70,y=140)
Deletee = Button(root,text = "Deletee",command=Deletee)
Deletee.place(x=130,y=140)
Get = Button(root,text = "Get",command=Get)
Get.place(x=190,y=140)






root.mainloop()

