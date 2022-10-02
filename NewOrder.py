from functools import partial
from operator import ge
from optparse import Values
from tkinter import *
from tkinter import ttk
from datetime import date, datetime
from traceback import print_tb
from tkcalendar import Calendar
import mysql.connector as sql

today = str(datetime.today())

mydb = sql.connect(host="localhost",
user= "root",
password ="admin",
database="zenithsales")

cursor =mydb.cursor()

def NewOrder():
    neworder =Tk()
    neworder.title("New Order")
    neworder.geometry("800x500")
    frame =Frame(neworder,height=max, bd=1,relief=FLAT)
    frame.pack(side=TOP,pady=30)

    def calender():
        def grad_date():
            dateoforder.delete(0,END)
            dateoforder.insert(0,cal.get_date())
            calenderwindow.destroy()
        calenderwindow = Tk()
        calenderwindow.geometry("300x300")
        calenderwindow.title("calendar")
        cal = Calendar(calenderwindow,selectmode = 'day',
                    year = datetime.now().year, 
                    month = datetime.now().month,
                    day = datetime.now().day, 
                    date_pattern = "yyyy-mm-dd")
        cal.pack(pady=20)
        cal.pack(pady = 20)
        select= Button(calenderwindow, text = "Get Date", command = grad_date).pack(pady = 20)

    def submit():
        query=("INSERT into orderStatus (partyName,Model,Finish,size,Quantity,dateOfOrder) values (%s,%s,%s,%s,%s,%s);")
        value=(PartyName.get(),model.get(),finish.get(),size.get(),quantity.get(),dateoforder.get())
        cursor.execute(query,value)
        mydb.commit()

        PartyName.delete(0,END)
        model.delete(0,END)
        finish.delete(0,END)
        size.delete(0,END)
        quantity.delete(0,END)
        dateoforder.delete(0,END)

    def searchParty(event):
        value =event.widget.get()
        if value=='':
            PartyName['values'] = partynames

        else:
            data=[]
            for item in partynames:
                if value.lower() in item.lower():
                    data.append(item)
            PartyName['values']=data

    def searchModel(event):
        value =event.widget.get()
        if value=='':
            model['values'] = models

        else:
            data=[]
            for item in models:
                if value.lower() in item.lower():
                    data.append(item)
            model['values']=data
    
    def searchSize(event):
        value =event.widget.get()
        if value=='':
            size['values'] = sizes

        else:
            data=[]
            for item in sizes:
                if value.lower() in item.lower():
                    data.append(item)
            size['values']=data
    
    def searchFinish(event):
        value =event.widget.get()
        if value=='':
            finish['values'] = finishes

        else:
            data=[]
            for item in finishes:
                if value.lower() in item.lower():
                    data.append(item)
            finish['values']=data

    partynames=[]
    models =[]
    finishes=[]
    sizes=[]
    
    cursor.execute("select distinct partyname from orderStatus  ;" )
    dataset=cursor.fetchall()
    for data in dataset:
        partynames.append(data[0])
    cursor.execute("select distinct model from orderStatus  ;" )
    dataset=cursor.fetchall()
    for data in dataset:
        models.append(data[0])
    cursor.execute("select distinct finish from orderStatus  ;" )
    dataset=cursor.fetchall()
    for data in dataset:
        finishes.append(data[0])
    cursor.execute("select distinct size from orderStatus  ;" )
    dataset=cursor.fetchall()
    for data in dataset:    
        sizes.append(data[0])

    #------------------------------------------------New Order Labels----------------------------------------------------------
    nameLabel= Label(frame, text ="party Name",font=("Segoe UI","14"))
    nameLabel.grid(row=0,column=0,padx=10,pady=5)
    ModelLabel= Label(frame, text ="Model",font=("Segoe UI","14"))
    ModelLabel.grid(row=1,column=0,padx=10,pady=5)
    finishingLabel= Label(frame, text ="Finishing",font=("Segoe UI","14"))
    finishingLabel.grid(row=2,column=0,padx=10,pady=5)
    sizeLabel= Label(frame, text ="Size",font=("Segoe UI","14"))
    sizeLabel.grid(row=3,column=0,padx=10,pady=5)
    quantityLabel= Label(frame, text ="Quantity",font=("Segoe UI","14"))
    quantityLabel.grid(row=4,column=0,padx=10,pady=5)
    dateLabel= Label(frame, text ="Date of Order",font=("Segoe UI","14"))
    dateLabel.grid(row=5,column=0,padx=10,pady=5)

    #--------------------------------------------New Order ComboBox--------------------------------------------------------
    PartyName = ttk.Combobox(frame,width=20,font=("Segoe UI","14"),values=partynames)
    PartyName.grid(row=0,column=1,padx=10,pady=5)
    PartyName.bind('<KeyRelease>',searchParty)
    model = ttk.Combobox(frame,width=20,font=("Segoe UI","14"),values=models)
    model.grid(row=1,column=1,padx=10,pady=5)
    model.bind('<KeyRelease>',searchModel)
    finish = ttk.Combobox(frame,width=20,font=("Segoe UI","14"),values=finishes)
    finish.grid(row=2,column=1,padx=10,pady=5)
    model.bind('<KeyRelease>',searchFinish)
    size = ttk.Combobox(frame,width=20,font=("Segoe UI","14"),values=sizes)
    size.grid(row=3,column=1,padx=10,pady=5)
    model.bind('<KeyRelease>',searchSize)
    quantity=Entry(frame,width=22,font=("Segoe UI","14"))
    quantity.grid(row=4,column=1,padx=10,pady=5)
    dateoforder =Entry(frame,width=22,font=("Segoe UI","14"))
    dateoforder.insert(0, today[:11])
    dateoforder.grid(row=5,column=1,padx=10,pady=5)


    cal_btn = Button(frame,text = "OPEN CALENDER",command = calender,font =('arial',8,'bold'),justify = LEFT)
    cal_btn.grid(row =6 ,column =1 ,pady =(0,20),sticky = E)

    Submit=Button(neworder,text="Submit",width=12,relief=RAISED,font=("Segoe UI",'18',"bold"),command=submit)
    Submit.pack(padx=10,pady=10,side=TOP)

    

    neworder.mainloop()