from tkinter import *
from tkinter import ttk
from datetime import date, datetime
from tkcalendar import Calendar
import mysql.connector as sql
today = str(datetime.today())

def MetalInput():
    neworder =Tk()
    neworder.title("New Metal input")
    neworder.geometry("1000x500")
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

    #------------------------------------------------Metal Input Label --------------------------------------------------------

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
    

    #------------------------------------------------------Vars---------------------------------------------------------
    model=StringVar()
    finish =StringVar()
    size = StringVar()
    #--------------------------------------------Metal Input ComboBox--------------------------------------------------------
    model = ttk.Combobox(frame,width=20,font=("Segoe UI","14"),textvariable=model)
    model.grid(row=1,column=1,padx=10,pady=5)
    finish = ttk.Combobox(frame,width=20,font=("Segoe UI","14"),textvariable=finish)
    finish.grid(row=2,column=1,padx=10,pady=5)
    size = ttk.Combobox(frame,width=20,font=("Segoe UI","14"),textvariable=size)
    size.grid(row=3,column=1,padx=10,pady=5)
    quantity = Text(frame,height=1,width=22,font=("Segoe UI","14"))
    quantity.grid(row=4,column=1,padx=10,pady=5)
    dateoforder =Entry(frame,width=22,font=("Segoe UI","14"))
    dateoforder.insert(0, today[:11])
    dateoforder.grid(row=5,column=1,padx=10,pady=5)

    cal_btn = Button(frame,text = "OPEN CALENDER",command = calender,font =('arial',8,'bold'),justify = LEFT)
    cal_btn.grid(row =6 ,column =1 ,pady =(0,20),sticky = E)

    Submit=Button(neworder,text="Submit",width=12,relief=RAISED,font=("Segoe UI",'18',"bold"),command="")
    Submit.pack(padx=10,pady=10,side=TOP)

    neworder.mainloop()