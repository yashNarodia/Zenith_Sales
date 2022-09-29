from tkinter import *
from tkinter import ttk
from datetime import date, datetime
from tkcalendar import Calendar
import mysql.connector as sql
from NewOrder import NewOrder
from MetalInput import MetalInput

today = str(datetime.today())

#shruti was here
#DATABASE Connection 
mydb = sql.connect(host="localhost",
user= "root",
password ="admin",
database="trial")
mycursor =mydb.cursor()


root = Tk()
root.title("Main Dashboard")
root.geometry("1910x800+0+0")
#FRAMES
Main_buttons = Frame(root, height=120, bd=1,relief=FLAT)
# Main_buttons.pack(side=TOP, fill ="x")
Main_buttons.grid(row=0)

Display=Frame(root,bd=1,height=750,relief=FLAT,highlightbackground="blue", highlightthickness=2)#highlightbackground="blue", highlightthickness=2
# Display.pack(side=TOP,fill="both")
Display.grid(row=1)
Sb= Scrollbar(Display, orient=VERTICAL)
Sb.grid(sticky=NS)

DisplayLabel=Label(Display,text="",font=("Segoe UI",'18',"bold"))
DisplayLabel.grid(row=0,columnspan=2)

query_label = Label(Display,text ="",width =45,justify = "center",font=("Segoe UI",'14'))
query_label.grid(row = 1, column =0)

#Logo
logo_img=PhotoImage(file='logo.png')
logo=Button(Main_buttons,relief=FLAT,width=50,height=50,image=logo_img)
logo.pack(padx=10,pady=10,side=LEFT,fill = BOTH, expand = True)

#----------------------------------------------BUTTON FUNCTIONS--------------------------------------------------------


    
def OrderStatus():
    DisplayLabel.config(text="Order Status")
    mycursor.execute("select * from trail;")
    orders =mycursor.fetchall()

    print_records=''
    for order in orders:
        for i in range (2):
            print_records +=str(order[i]) + "   "
        print_records += "\n"
    query_label.config(text=print_records)
        
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
def Turning():
    DisplayLabel.config(text="At Turning Stage")
    return
def Finishing():
    DisplayLabel.config(text="At Finishing Stage")
    
def Stock():
    DisplayLabel.config(text="Stocks")
    return

#--------------------------------------------MAIN BUTTON----------------------------------------------------------------------
NewOrder=Button(Main_buttons,text="New Order",width=12,relief=RAISED,font=("Segoe UI",'18',"bold"),command=NewOrder)
NewOrder.pack(padx=10,pady=10,side=LEFT,fill = BOTH, expand = True)

MetalInput=Button(Main_buttons,text="Metal Input",width=12,relief=RAISED,font=("Segoe UI",'18',"bold"),command=MetalInput)
MetalInput.pack(padx=10,pady=10,side=LEFT,fill = BOTH, expand = True)

OrderStatus=Button(Main_buttons,text="Order Status",width=12,relief=RAISED,font=("Segoe UI",'18',"bold"),command=OrderStatus)
OrderStatus.pack(padx=10,pady=10,side=LEFT,fill = BOTH, expand = True)

CastingProcess=Button(Main_buttons,text="Casting",width=12,relief=RAISED,font=("Segoe UI",'18',"bold"),command=Casting)
CastingProcess.pack(padx=10,pady=10,side=LEFT,fill = BOTH, expand = True)

TurningProcess=Button(Main_buttons,text="Turning",width=12,relief=RAISED,font=("Segoe UI",'18',"bold"),command=Turning)
TurningProcess.pack(padx=10,pady=10,side=LEFT,fill = BOTH, expand = True) 

FinishingProcess=Button(Main_buttons,text="Finishing",width=12,relief=RAISED,font=("Segoe UI",'18',"bold"),command=Finishing)
FinishingProcess.pack(padx=10,pady=10,side=LEFT,fill = BOTH, expand = True) 

Stock=Button(Main_buttons,text="Stock",width=12,relief=RAISED,font=("Segoe UI",'18',"bold"),command=Stock)
Stock.pack(padx=10,pady=10,side=LEFT,fill = BOTH, expand = True)





root.mainloop()