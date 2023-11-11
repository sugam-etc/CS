from tkinter import *
from Data import *
import threading
import sqlite3 as sq
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
plt.rcParams['toolbar'] = 'None'

#Connecting with dataBase
connection = sq.connect("abc.db")
cursor = connection.cursor()  #will be doing everything on it
cursor.execute("create table if not exists students ( symbol , full_name , address, username , password,grades,rollno,mode_of_login)")
cursor.executemany("insert into students values (?,?,?,?,?,?,?,?)",students_data)
#Creating Root File
root = Tk()
root.title("School Management System")
root.geometry("1920x1280")
root.configure(bg="#B2BDC4")
# root.resizable(False,False)

#Header1 (School Management System)
Label(text='',bg='#C5DCA0').pack()
header = Label(root,
            text="School Management System",
            relief=GROOVE,
            font=('Arial',60,'bold'),
            border=10,
            bg='#3C7A89',
            fg='#fff',
            pady=50)
header.pack(side=TOP)
# def plot():
#     x = [2079,2079,2080]
#     y = [3.5,3.2,3.6]
#     plt.plot(x,y)
#     plt.xlabel('Year')
#     plt.ylabel('Average Grade Points')
#     plt.show()
#functions for Login
def mainhomepage():
    print("Main Home Page Opened")
    global main_root
    main_root = Tk()
    main_root.title("School Management System")
    main_root.geometry("1920x1280")
    main_root.configure(bg="#B2BDC4")
    Label(main_root,
            text="School Management System",
            relief=GROOVE,
            font=('Arial',60,'bold'),
            border=10,
            bg='#3C7A89',
            fg='#9FA2B2',
            pady=50).pack(side=TOP)

    def plotgraph():
            x = [2079,2079,2080]
            y = [3.5,3.2,3.6]
            plt.plot(x,y)
            plt.xlabel('Year')
            plt.ylabel('Average Grade Points')
            plt.show()

            Button(master = main_root, 
                     command = plot,
                     height = 2, 
                     width = 10,
                     text = "Plot").pack()

  
# place the button 
# in main window
    
    



    main_root.mainloop()
def onRegister():
       
        global count
        count = 0
        for item in cursor.execute("select * from students"):
            count = count + 1
        print(count)
        tempu = ((count + 1),full_name.get(),address.get(),new_username.get(),new_password.get(),grades.get(),roll_no.get(),1)
        cursor.execute(f"insert into students values (?,?,?,?,?,?,?,?)",tempu)

        
        for item in cursor.execute(f"select * from students where symbol = {count}"):
            print(item)
        connection.commit()
        mainhomepage()
def register():
    wn.destroy()
    global register_window
    global full_name
    global address
    global grades
    global roll_no
    global new_username
    global new_password
    print("Register Window Opened")
    register_window = Tk()
    register_window.geometry('1920x1280')
    register_window.resizable(False,False)
    register_window.config(bg='#B2BDC4')
    Label(text="",bg='#B2BDC4').pack()
    Label(text="Register Your Account",font=('Calibri',40,'bold'),bg='#B2BDC4').pack()
    full_name = StringVar()
    address = StringVar()
    roll_no = StringVar()
    grades = StringVar()
    new_username = StringVar()
    new_password = StringVar()
    Label(text="",bg='#B2BDC4').pack()
    Label(text="Full Name",font=('Arial',20,'bold'),bg='#B2BDC4').pack()
    Label(text="",bg='#B2BDC4').pack()
    Entry(font=('Arial',20,'bold'),textvariable=full_name,bg='#B2BDC4').pack()
    Label(text="Address",font=('Arial',20,'bold'),bg='#B2BDC4').pack()
    Label(text="",bg='#B2BDC4').pack()
    Entry(font=('Arial',20,'bold'),textvariable=address,bg='#B2BDC4').pack()
    Label(text="RollNO",font=('Arial',20,'bold'),bg='#B2BDC4').pack()
    Label(text="",bg='#B2BDC4').pack()
    Entry(font=('Arial',20,'bold'),textvariable=roll_no,bg='#B2BDC4').pack()
    Label(text="Grades",font=('Arial',20,'bold'),bg='#B2BDC4').pack()
    Label(text="",bg='#B2BDC4').pack()
    Entry(font=('Arial',20,'bold'),textvariable=grades,bg='#B2BDC4').pack()
    Label(text="Username",font=('Arial',20,'bold'),bg='#B2BDC4').pack()
    Label(text="",bg='#B2BDC4').pack()
    Entry(font=('Arial',20,'bold'),textvariable=new_username,bg='#B2BDC4').pack()
    Label(text="Password",font=('Arial',20,'bold'),bg='#B2BDC4').pack()
    Label(text="",bg='#B2BDC4').pack()
    Entry(font=('Arial',20,'bold'),textvariable=new_password,bg='#B2BDC4').pack()
    Label(text='',bg='#B2BDC4').pack()
    Button(text='Register',command=onRegister,font=('Arial',20,'bold'),bg='#818AA3',fg='#fff').pack()
    Label(text='',bg='#B2BDC4').pack()
    Label(text='',bg='#B2BDC4').pack()
    register_window.mainloop()
def onUnAuthentication(rootvar):
    Label(rootvar,text='Check Details Properly',fg='red').pack()




def login():
    wn.destroy()
    global login_window
    login_window = Tk()
    login_window.title('Login')
    login_window.geometry('600x600')
    global username
    global password
    global mode_of_login
    print("Login Window Opened")
    username = StringVar()
    password = StringVar()
    mode_of_login = IntVar()
    Label(text='Login',font=('Calibri',50,'bold')).pack()
    Label(text="").pack()
    Label(text="UserName:",font=('Arial',30,'bold')).pack()
    Entry(width=20,font=('Calibri',30,'bold'),textvariable=username).pack()
    Label(text="Password:",font=('Arial',30,'bold')).pack()
    Entry(show="*",font=('Calibri',30,'bold'),textvariable=password).pack()
    Label(text="").pack()
    Radiobutton(text="Student",variable=mode_of_login,value=1,font=('Calibri',15,'bold')).pack()
    Radiobutton(text="Staff/Teacher",variable=mode_of_login,value=2,font=('Calibri',15,'bold')).pack()
    Label(text="").pack()

    #Function on Submittion of id and pass
    def onSubmit():
        print("submitted")
    # print(username.get())
    # print(password.get())
    # print(mode_of_login.get())
    # login_window.destroy()
        for item in cursor.execute("select * from students"):
            if(item[3]== username.get() and item[4] == password.get() and int(item[7]) == mode_of_login.get()):
                login_window.destroy()
                mainhomepage()
                break
                
        else:
            # temp = threading.Timer(3.0,onUnAuthentication(login_window))
            # temp.start()
            onUnAuthentication(login_window)
        
    Button(text="Submit",relief=RAISED,font=('Calibri',20,'bold'),command=onSubmit).pack()
    login_window.mainloop()

def choosing_login_method():
    print("CHoosing Login MEthod")
    global wn
    wn = Tk()
    wn.geometry('600x600')
    wn.title('Login Form')
    wn.config(bg='#2E4756')
    Label(wn,text="Choose Login Method",font=('Arial',40,'bold'),bg='#2E4756',fg='#fff').pack()
    Label(text="",bg='#2E4756').pack()
    Button(wn,text="Login",relief=GROOVE,command=login,font=('Calibri',40,'bold'),bg='#C5DCA0',activebackground='#1F2041',activeforeground='#FFF8EB').pack()
    Label(text="",bg='#2E4756').pack()
    Button(wn,text="Register",relief=GROOVE,command=register,font=('Calibri',40,'bold'),bg='#C5DCA0',activebackground='#1F2041',activeforeground='#FFF8EB').pack()
    wn.mainloop()
def onCheckIn():
    root.destroy()
    choosing_login_method()


#Check In Button 
checkin_btn = Button(root,text="CheckIn",font=('Arial',40,'bold'),padx=20,relief=GROOVE,border=5,activebackground='black',activeforeground='white',command=onCheckIn,state=DISABLED)
checkin_btn.pack(side=BOTTOM)
Label(text='',bg="#C5DCA0").pack(side=BOTTOM)

#CheckBox (Terms And Conditions)
x = IntVar()
def checkin_btn_state():
    if(x.get() == 0):
        checkin_btn['state'] = DISABLED
    elif(x.get() == 1):
        checkin_btn['state'] = NORMAL
checkbox_init = Checkbutton(root,text='I agree to terms and conditions',variable=x,onvalue=1,offvalue=0,cursor='pencil',font=('Arial',20,'bold'),command=checkin_btn_state)
checkbox_init.pack(side=BOTTOM)






root.mainloop()
        


# root.mainloop()
connection.close()
