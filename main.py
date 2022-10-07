from tkinter import *
from tkinter import ttk
from datetime import date, datetime
from tkcalendar import Calendar
import mysql.connector as sql
from NewOrder import NewOrder
from MetalInput import MetalInput

today = str(datetime.today())

#DATABASE Connection 
mydb = sql.connect(host="localhost",
user= "root",
password ="admin",
database="zenithsales")
mycursor =mydb.cursor()

root = Tk()
root.title("Main Dashboard")
root.geometry("1910x800+0+0")
#FRAMES
Main_buttons = Frame(root, height=120, bd=1,relief=FLAT)
Main_buttons.pack(side=TOP, fill ="x",padx=5, pady=5)
# Main_buttons.grid(row=0)

Display=Frame(root,bd=1,height=800,relief=FLAT)
Display.pack(side=TOP,padx=5,pady=5)
# Display.grid(row=1)
updation_buttons=Frame(root, bd=1,height=100,relief=FLAT)#,highlightbackground="red", highlightthickness=2
updation_buttons.pack(side=TOP,padx=20,pady=5)
# updation_buttons.grid(row=2,pady=20)
DisplayLabel=Label(Display,text="Zenith Sales",font=("Segoe UI",'18',"bold"))
DisplayLabel.pack(side=TOP)
# DisplayLabel.grid(row=0,columnspan=2)

# query_label = Label(Display,text ="Welcome sir, have a Great Day!",width =45,justify = "center",font=("Segoe UI",'14'))
# query_label.grid(row = 1, column =0)

#Logo
logo_img=PhotoImage(file='logo.png')
logo=Button(Main_buttons,relief=FLAT,width=50,height=50,image=logo_img)
logo.pack(padx=10,pady=10,side=LEFT,fill = BOTH, expand = True)

style =ttk.Style()
style.theme_use('default')

style.configure('Treeview',
Background ='#d3d3d3',
foreground = 'black',
rowheight =30,
fieldbackground ='#d3d3d3',
font=("Segoe UI",'16'))

style.configure('Treeview.Heading',font=("Segoe UI",'18','bold'))
style.map("Treeview",
background=[('selected',"#347083")])


#----------------------------------------------BUTTON FUNCTIONS--------------------------------------------------------


treeframe =Frame(Display)
treeframe.pack(padx=10, pady=10)
treescroll = Scrollbar(treeframe,)


mytree = ttk.Treeview(treeframe,yscrollcommand=treescroll.set,selectmode='extended')

treescroll.config(command=mytree.yview)
    
def OrderStatus():
    for widget in updation_buttons.winfo_children():
        widget.destroy()
    treescroll.pack(side=RIGHT,fill=Y)
    mytree.pack(pady=10)
    DisplayLabel.config(text="Order Status")

    mytree['columns'] = ("Party Name", "Model", "Finish","Size", "Quantity", "Date of Order", "Status")

    mytree.column("#0",width=0,stretch=0)
    mytree.column("Party Name",anchor=CENTER,width=180)
    mytree.column("Model",anchor=CENTER,width=180)
    mytree.column("Finish",anchor=CENTER,width=180)
    mytree.column("Size",anchor=CENTER,width=180)
    mytree.column("Quantity",anchor=CENTER,width=150)
    mytree.column("Date of Order",anchor=CENTER,width= 180)
    mytree.column("Status",anchor=CENTER,width=150)

    mytree.heading('#0',text='',anchor=CENTER)
    mytree.heading("Party Name",text="Party Name",anchor=CENTER)
    mytree.heading("Model",text="Model",anchor=CENTER)
    mytree.heading("Finish",text="Finish",anchor=CENTER)
    mytree.heading("Size",text="Size",anchor=CENTER)
    mytree.heading("Quantity",text="Quantity",anchor=CENTER)
    mytree.heading("Date of Order",text="Date of Order",anchor=CENTER)
    mytree.heading("Status",text="Status",anchor=CENTER)

    mycursor.execute("select * from orderStatus;")
    orders =mycursor.fetchall()
    for i in mytree.get_children():
        mytree.delete(i)

    mytree.tag_configure('oddrow',background="skyblue")
    mytree.tag_configure('evenrow',background="white")
    global count
    count =0

    for order in orders:
        order = list(order)
        order[5] = order[5].strftime("%d-%m-%Y")
        if order[6]==0:
            order[6]="Pending"
        else:
            order[6]="Completed"
        
        if count % 2 == 0:
            mytree.insert(parent='',index='end',iid=count,text='',values=(order[0],order[1],order[2],order[3],order[4],order[5],order[6]),tags=('evenrow',))
        else:
            mytree.insert(parent='',index='end',iid=count,text='',values=(order[0],order[1],order[2],order[3],order[4],order[5],order[6]),tags=('oddrow',))
        count+=1

    nameLabel= Label(updation_buttons, text ="party Name",font=("Segoe UI","14"))
    nameLabel.grid(row=0,column=0,padx=10,pady=5)
    ModelLabel= Label(updation_buttons, text ="Model",font=("Segoe UI","14"))
    ModelLabel.grid(row=1,column=0,padx=10,pady=5)
    finishingLabel= Label(updation_buttons, text ="Finishing",font=("Segoe UI","14"))
    finishingLabel.grid(row=2,column=0,padx=10,pady=5)
    sizeLabel= Label(updation_buttons, text ="Size",font=("Segoe UI","14"))
    sizeLabel.grid(row=0,column=2,padx=10,pady=5)
    quantityLabel= Label(updation_buttons, text ="Quantity",font=("Segoe UI","14"))
    quantityLabel.grid(row=1,column=2,padx=10,pady=5)
    dateLabel= Label(updation_buttons, text ="Date of Order",font=("Segoe UI","14"))
    dateLabel.grid(row=2,column=2,padx=10,pady=5)

    PartyName = Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    PartyName.grid(row=0,column=1,padx=10,pady=5)
    model = Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    model.grid(row=1,column=1,padx=10,pady=5)
    finish = Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    finish.grid(row=2,column=1,padx=10,pady=5)
    size = Entry(updation_buttons,width=22,font=("Segoe UI","14"))
    size.grid(row=0,column=3,padx=10,pady=5)
    quantity=Entry(updation_buttons,width=22,font=("Segoe UI","14"))
    quantity.grid(row=1,column=3,padx=10,pady=5)
    dateoforder =Entry(updation_buttons,width=22,font=("Segoe UI","14"))
    dateoforder.grid(row=2,column=3,padx=10,pady=5)

    Updatebtn = Button(updation_buttons,text="Update",width=20,font=("Segoe UI","14"))
    Updatebtn.grid(row=3, columnspan= 2,column=0 ,padx=10,pady=10 )  
    completebtn = Button(updation_buttons,text="Complete Order",width=20,font=("Segoe UI","14"))
    completebtn.grid(row=3, columnspan= 2,column=2 ,padx=10,pady=10 )  

    def select_record(e):
        PartyName.delete(0,END)
        model.delete(0,END)
        finish.delete(0,END)
        size.delete(0,END)
        quantity.delete(0,END)
        dateoforder.delete(0,END)

        selected =mytree.focus()
        values=mytree.item(selected,'values')

        PartyName.insert(0,values[0])
        model.insert(0,values[1])
        finish.insert(0,values[2])
        size.insert(0,values[3])
        quantity.insert(0,values[4])
        dateoforder.insert(0,values[5])

    mytree.bind("<ButtonRelease-1>",select_record)

def Casting():
    for widget in updation_buttons.winfo_children():
        widget.destroy()
    treescroll.pack(side=RIGHT,fill=Y)
    mytree.pack(pady=10)
    DisplayLabel.config(text="At Casting Stage")
    mycursor.execute("select model, finish, size, quantity, dateoforder from metalInput where casting = 1 AND turning = 0 AND finishing = 0 AND stock = 0;")
    orders =mycursor.fetchall()
    for i in mytree.get_children():
        mytree.delete(i)


    mytree['columns'] = ("Model", "Finish","Size", "Quantity", "Date of Order")

    mytree.column("#0",width=0,stretch=0)
    mytree.column("Model",anchor=CENTER,width=200)
    mytree.column("Finish",anchor=CENTER,width=200)
    mytree.column("Size",anchor=CENTER,width=200)
    mytree.column("Quantity",anchor=CENTER,width=200)
    mytree.column("Date of Order",anchor=CENTER,width= 200)

    mytree.heading('#0',text='',anchor=CENTER)
    mytree.heading("Model",text="Model",anchor=CENTER)
    mytree.heading("Finish",text="Finish",anchor=CENTER)
    mytree.heading("Size",text="Size",anchor=CENTER)
    mytree.heading("Quantity",text="Quantity",anchor=CENTER)
    mytree.heading("Date of Order",text="Date of Order",anchor=CENTER)

    global count
    count =0

    for order in orders:
        order = list(order)
        order[4] = order[4].strftime("%d-%m-%Y")
        if count % 2 == 0:
            mytree.insert(parent='',index='end',iid=count,text='',values=(order[0],order[1],order[2],order[3],order[4]),tags=('evenrow',))
        else:
            mytree.insert(parent='',index='end',iid=count,text='',values=(order[0],order[1],order[2],order[3],order[4]),tags=('oddrow',))
        count+=1

    ModelLabel= Label(updation_buttons, text ="Model",font=("Segoe UI","14"))
    ModelLabel.grid(row=1,column=0,padx=10,pady=5)
    finishingLabel= Label(updation_buttons, text ="Finishing",font=("Segoe UI","14"))
    finishingLabel.grid(row=1,column=3,padx=10,pady=5)
    sizeLabel= Label(updation_buttons, text ="Size",font=("Segoe UI","14"))
    sizeLabel.grid(row=2,column=3,padx=10,pady=5)
    quantityLabel= Label(updation_buttons, text ="Quantity",font=("Segoe UI","14"))
    quantityLabel.grid(row=2,column=0,padx=10,pady=5)
    dateLabel= Label(updation_buttons, text ="Date of Order",font=("Segoe UI","14"))
    dateLabel.grid(row=3,column=0,padx=10,pady=5)

    model = Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    model.grid(row=1,column=1,padx=10,pady=5)
    finish = Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    finish.grid(row=1,column=4,padx=10,pady=5)
    size = Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    size.grid(row=2,column=1,padx=10,pady=5)
    quantity = Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    quantity.grid(row=2,column=4,padx=10,pady=5)
    dateoforder =Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    dateoforder.grid(row=3,column=1,padx=10,pady=5)
    castingcheck= Checkbutton(updation_buttons,text="Casting",variable='castingcheck',font=("Segoe UI","14"),onvalue=1,offvalue=0,width=20)
    castingcheck.grid(row=3,column=3,columnspan=2) 
    Updatebtn = Button(updation_buttons,text="Update",width=20,font=("Segoe UI","14"))
    Updatebtn.grid(row=4, columnspan= 6 ,padx=10,pady=10 )   

    def select_record(e):
        model.delete(0,END)
        finish.delete(0,END)
        size.delete(0,END)
        quantity.delete(0,END)
        dateoforder.delete(0,END)

        selected =mytree.focus()
        values=mytree.item(selected,'values')

        model.insert(0,values[0])
        finish.insert(0,values[1])
        size.insert(0,values[2])
        quantity.insert(0,values[3])
        dateoforder.insert(0,values[4])

    mytree.bind("<ButtonRelease-1>",select_record)

def Turning():
    for widget in updation_buttons.winfo_children():
        widget.destroy()
    treescroll.pack(side=RIGHT,fill=Y)
    mytree.pack(pady=10)
    DisplayLabel.config(text="At Turning Stage")
    mycursor.execute("select model, finish, size, quantity, dateoforder from metalInput where turning = 1 AND finishing = 0 AND stock = 0;")
    orders =mycursor.fetchall()
    for i in mytree.get_children():
        mytree.delete(i)

    mytree['columns'] = ("Model", "Finish","Size", "Quantity", "Date of Order")

    mytree.column("#0",width=0,stretch=0)
    mytree.column("Model",anchor=CENTER,width=200)
    mytree.column("Finish",anchor=CENTER,width=200)
    mytree.column("Size",anchor=CENTER,width=200)
    mytree.column("Quantity",anchor=CENTER,width=200)
    mytree.column("Date of Order",anchor=CENTER,width= 200)

    mytree.heading('#0',text='',anchor=CENTER)
    mytree.heading("Model",text="Model",anchor=CENTER)
    mytree.heading("Finish",text="Finish",anchor=CENTER)
    mytree.heading("Size",text="Size",anchor=CENTER)
    mytree.heading("Quantity",text="Quantity",anchor=CENTER)
    mytree.heading("Date of Order",text="Date of Order",anchor=CENTER)

    global count
    count =0

    for order in orders:
        order = list(order)
        order[4] = order[4].strftime("%d-%m-%Y")
        if count % 2 == 0:
            mytree.insert(parent='',index='end',iid=count,text='',values=(order[0],order[1],order[2],order[3],order[4]),tags=('evenrow',))
        else:
            mytree.insert(parent='',index='end',iid=count,text='',values=(order[0],order[1],order[2],order[3],order[4]),tags=('oddrow',))
        count+=1

    ModelLabel= Label(updation_buttons, text ="Model",font=("Segoe UI","14"))
    ModelLabel.grid(row=1,column=0,padx=10,pady=5)
    finishingLabel= Label(updation_buttons, text ="Finishing",font=("Segoe UI","14"))
    finishingLabel.grid(row=1,column=3,padx=10,pady=5)
    sizeLabel= Label(updation_buttons, text ="Size",font=("Segoe UI","14"))
    sizeLabel.grid(row=2,column=3,padx=10,pady=5)
    quantityLabel= Label(updation_buttons, text ="Quantity",font=("Segoe UI","14"))
    quantityLabel.grid(row=2,column=0,padx=10,pady=5)
    dateLabel= Label(updation_buttons, text ="Date of Order",font=("Segoe UI","14"))
    dateLabel.grid(row=3,column=0,padx=10,pady=5)

    model = Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    model.grid(row=1,column=1,padx=10,pady=5)
    finish = Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    finish.grid(row=1,column=4,padx=10,pady=5)
    size = Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    size.grid(row=2,column=1,padx=10,pady=5)
    quantity = Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    quantity.grid(row=2,column=4,padx=10,pady=5)
    dateoforder =Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    dateoforder.grid(row=3,column=1,padx=10,pady=5)
    turningcheck= Checkbutton(updation_buttons,text="Turning",variable='turningcheck',font=("Segoe UI","14"),onvalue=1,offvalue=0,width=20)
    turningcheck.grid(row=3,column=3,columnspan=2)
    Updatebtn = Button(updation_buttons,text="Update",width=20,font=("Segoe UI","14"))
    Updatebtn.grid(row=4, columnspan= 6,padx=10,pady=10 )

    def select_record(e):
        model.delete(0,END)
        finish.delete(0,END)
        size.delete(0,END)
        quantity.delete(0,END)
        dateoforder.delete(0,END)

        selected =mytree.focus()
        values=mytree.item(selected,'values')

        model.insert(0,values[0])
        finish.insert(0,values[1])
        size.insert(0,values[2])
        quantity.insert(0,values[3])
        dateoforder.insert(0,values[4])

    mytree.bind("<ButtonRelease-1>",select_record)

def Finishing():
    for widget in updation_buttons.winfo_children():
        widget.destroy()
    treescroll.pack(side=RIGHT,fill=Y)
    mytree.pack(pady=10)
    DisplayLabel.config(text="At Finishing Stage")
    mycursor.execute("select model, finish, size, quantity, dateoforder from metalInput where finishing = 1 AND stock = 0;")
    orders =mycursor.fetchall()
    
    for i in mytree.get_children():
        mytree.delete(i)


    mytree['columns'] = ("Model", "Finish","Size", "Quantity", "Date of Order")

    mytree.column("#0",width=0,stretch=0)
    mytree.column("Model",anchor=CENTER,width=200)
    mytree.column("Finish",anchor=CENTER,width=200)
    mytree.column("Size",anchor=CENTER,width=200)
    mytree.column("Quantity",anchor=CENTER,width=200)
    mytree.column("Date of Order",anchor=CENTER,width= 200)

    mytree.heading('#0',text='',anchor=CENTER)
    mytree.heading("Model",text="Model",anchor=CENTER)
    mytree.heading("Finish",text="Finish",anchor=CENTER)
    mytree.heading("Size",text="Size",anchor=CENTER)
    mytree.heading("Quantity",text="Quantity",anchor=CENTER)
    mytree.heading("Date of Order",text="Date of Order",anchor=CENTER)

    global count
    count =0

    for order in orders:
        order = list(order)
        order[4] = order[4].strftime("%d-%m-%Y")
        if count % 2 == 0:
            mytree.insert(parent='',index='end',iid=count,text='',values=(order[0],order[1],order[2],order[3],order[4]),tags=('evenrow',))
        else:
            mytree.insert(parent='',index='end',iid=count,text='',values=(order[0],order[1],order[2],order[3],order[4]),tags=('oddrow',))
        count+=1
    ModelLabel= Label(updation_buttons, text ="Model",font=("Segoe UI","14"))
    ModelLabel.grid(row=1,column=0,padx=10,pady=5)
    finishingLabel= Label(updation_buttons, text ="Finishing",font=("Segoe UI","14"))
    finishingLabel.grid(row=1,column=3,padx=10,pady=5)
    sizeLabel= Label(updation_buttons, text ="Size",font=("Segoe UI","14"))
    sizeLabel.grid(row=2,column=3,padx=10,pady=5)
    quantityLabel= Label(updation_buttons, text ="Quantity",font=("Segoe UI","14"))
    quantityLabel.grid(row=2,column=0,padx=10,pady=5)
    dateLabel= Label(updation_buttons, text ="Date of Order",font=("Segoe UI","14"))
    dateLabel.grid(row=3,column=0,padx=10,pady=5)

    model = Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    model.grid(row=1,column=1,padx=10,pady=5)
    finish = Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    finish.grid(row=1,column=4,padx=10,pady=5)
    size = Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    size.grid(row=2,column=1,padx=10,pady=5)
    quantity = Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    quantity.grid(row=2,column=4,padx=10,pady=5)
    dateoforder =Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    dateoforder.grid(row=3,column=1,padx=10,pady=5)
    finishcheck= Checkbutton(updation_buttons,text="Finish",variable='finishcheck',font=("Segoe UI","14"),onvalue=1,offvalue=0,width=20)
    finishcheck.grid(row=3,column=3,columnspan=2) 
    Updatebtn = Button(updation_buttons,text="Update",width=20,font=("Segoe UI","14"))
    Updatebtn.grid(row=4, columnspan= 6,padx=10,pady=10 )

    def select_record(e):
        model.delete(0,END)
        finish.delete(0,END)
        size.delete(0,END)
        quantity.delete(0,END)
        dateoforder.delete(0,END)

        selected =mytree.focus()
        values=mytree.item(selected,'values')

        model.insert(0,values[0])
        finish.insert(0,values[1])
        size.insert(0,values[2])
        quantity.insert(0,values[3])
        dateoforder.insert(0,values[4])

    mytree.bind("<ButtonRelease-1>",select_record)

def Stock():
    for widget in updation_buttons.winfo_children():
        widget.destroy()
    treescroll.pack(side=RIGHT,fill=Y)
    mytree.pack(pady=10)
    DisplayLabel.config(text="Stocks")
    mycursor.execute("select model, finish, size, quantity, dateoforder from metalInput where stock = 1;")
    orders =mycursor.fetchall()

    for i in mytree.get_children():
        mytree.delete(i)


    mytree['columns'] = ("Model", "Finish","Size", "Quantity", "Date of Order")

    mytree.column("#0",width=0,stretch=0)
    mytree.column("Model",anchor=CENTER,width=200)
    mytree.column("Finish",anchor=CENTER,width=200)
    mytree.column("Size",anchor=CENTER,width=200)
    mytree.column("Quantity",anchor=CENTER,width=200)
    mytree.column("Date of Order",anchor=CENTER,width= 200)

    mytree.heading('#0',text='',anchor=CENTER)
    mytree.heading("Model",text="Model",anchor=CENTER)
    mytree.heading("Finish",text="Finish",anchor=CENTER)
    mytree.heading("Size",text="Size",anchor=CENTER)
    mytree.heading("Quantity",text="Quantity",anchor=CENTER)
    mytree.heading("Date of Order",text="Date of Order",anchor=CENTER)

    global count
    count =0

    for order in orders:
        order = list(order)
        order[4] = order[4].strftime("%d-%m-%Y")
        if count % 2 == 0:
            mytree.insert(parent='',index='end',iid=count,text='',values=(order[0],order[1],order[2],order[3],order[4]),tags=('evenrow',))
        else:
            mytree.insert(parent='',index='end',iid=count,text='',values=(order[0],order[1],order[2],order[3],order[4]),tags=('oddrow',))
        count+=1

    ModelLabel= Label(updation_buttons, text ="Model",font=("Segoe UI","14"))
    ModelLabel.grid(row=1,column=0,padx=10,pady=5)
    finishingLabel= Label(updation_buttons, text ="Finishing",font=("Segoe UI","14"))
    finishingLabel.grid(row=1,column=3,padx=10,pady=5)
    sizeLabel= Label(updation_buttons, text ="Size",font=("Segoe UI","14"))
    sizeLabel.grid(row=2,column=3,padx=10,pady=5)
    quantityLabel= Label(updation_buttons, text ="Quantity",font=("Segoe UI","14"))
    quantityLabel.grid(row=2,column=0,padx=10,pady=5)
    dateLabel= Label(updation_buttons, text ="Date of Order",font=("Segoe UI","14"))
    dateLabel.grid(row=3,column=0,padx=10,pady=5)

    model = Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    model.grid(row=1,column=1,padx=10,pady=5)
    finish = Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    finish.grid(row=1,column=4,padx=10,pady=5)
    size = Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    size.grid(row=2,column=1,padx=10,pady=5)
    quantity = Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    quantity.grid(row=2,column=4,padx=10,pady=5)
    dateoforder =Entry(updation_buttons,width=20,font=("Segoe UI","14"))
    dateoforder.grid(row=3,column=1,padx=10,pady=5)

    Updatebtn = Button(updation_buttons,text="Update",width=20,font=("Segoe UI","14"))
    Updatebtn.grid(row=4, columnspan= 5,padx=10,pady=10 )

    def select_record(e):
        model.delete(0,END)
        finish.delete(0,END)
        size.delete(0,END)
        quantity.delete(0,END)
        dateoforder.delete(0,END)

        selected =mytree.focus()
        values=mytree.item(selected,'values')

        model.insert(0,values[0])
        finish.insert(0,values[1])
        size.insert(0,values[2])
        quantity.insert(0,values[3])
        dateoforder.insert(0,values[4])

    mytree.bind("<ButtonRelease-1>",select_record)

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