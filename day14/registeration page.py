from tkinter import *
import tkinter.messagebox  as msg
import mysql.connector as mysql
root=Tk()
root.title("Registration page")

def database():
    b=mysql.connect(host="localhost",user="root", password="123456")
    cursor=b.cursor()
    cursor.execute("create database registeration ;")
    cursor.execute("use registeration")
    cursor.execute("create table info (name char(10),dob date,username varchar(10),password int(10));")

def sql():
    Name=nam.get()
    username=usnam.get()
    Dob=dob.get()
    password=pas.get()
    confirm=cpas.get()
    if (Name=="" or Dob==""or username=="" or password=="" or confirm==""):
        msg.showinfo("error","all fields are required")
    elif (password != confirm):
        msg.showinfo("error","password and confirm password must be same")
    else:
        a=mysql.connect(host="localhost",user="root", password="123456",database="registeration")
        cursor=a.cursor()
        cursor.execute(f"insert into info values('{nam.get()}','{dob.get()}','{usnam.get()}','{pas.get()}');")
        a.commit()
        a.close()
        msg.showinfo("Done","data added")
def getval():
    print("submitted")
    with open("reg.txt","a") as f:
        f.write((f"name is {nam.get()}\n")),
        f.write((f"username is {usnam.get()}\n")),
        f.write((f"dob is {dob.get()}\n")),
        f.write((f"password is {pas.get()}\n")),
        f.write((f"confirm password is {cpas.get()}\n")),

Name=Label(root,text="Name")
Name.grid(row=1,column=0)
userName=Label(root,text="Username")
userName.grid(row=2,column=0)

dob=Label(root,text="dob")
dob.grid(row=3,column=0)

password=Label(root,text="Password")
password.grid(row=4,column=0)

cpass=Label(root,text="confirm password")
cpass.grid(row=5,column=0)

nameentry=StringVar()
usernameentry=StringVar()
dobentry=StringVar()
rollentry=StringVar()
genderentry=StringVar()

nam=Entry(root,textvariable=nameentry)
usnam=Entry(root,textvariable=usernameentry)
dob=Entry(root,textvariable=dobentry)
pas=Entry(root,textvariable=rollentry)
cpas=Entry(root,textvariable=genderentry)

nam.grid(row=1,column=1)
usnam.grid(row=2,column=1)
dob.grid(row=3,column=1)
pas.grid(row=4,column=1)
cpas.grid(row=5,column=1)

Button(root,text="submit",command=getval).grid(row=6,column=2,padx=10)
Button(root,text="create db",command=database).grid(row=6,column=0)
Button(root,text="add data",command=sql).grid(row=6,column=1)

root.geometry("300x200")
root.mainloop()