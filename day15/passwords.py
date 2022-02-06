from tkinter import *
import mysql.connector as mysql
import tkinter.messagebox as msg

root=Tk()
root.title("Login")

def database():
    b=mysql.connect(host="localhost",user="root", password="123456")
    cursor=b.cursor()
    cursor.execute("create database Passwords ;")
    cursor.execute("use Passwords")
    cursor.execute("create table info (email char(255),password blob);")

def sql():
    Email=email.get()
    password=pas.get()
    if (Email=="" or password==""):
        msg.showinfo("error","all fields are required")
    else:
        a=mysql.connect(host="localhost",user="root", password="123456",database="Passwords")
        cursor=a.cursor()
        cursor.execute(f"insert into info values('{email.get()}','{pas.get()}');")
        a.commit()
        a.close()
        msg.showinfo("Done","data added")
        getval()
    
def getval():
    print("submitted")
    with open("pass.txt","a") as f:
        f.write((f"Email is {email.get()}\n")),
        f.write((f"password is {pas.get()}\n")),

username=Label(root,text="Email",font="cursive 13 bold")
username.grid(row=0,column=0)

password=Label(root,text="Password",font="cursive 13 bold")
password.grid(row=2,column=0)

userval=StringVar()
passval=StringVar()

email=Entry(root,textvariable=userval)
pas=Entry(root,textvariable=passval)
email.grid(row=0,column=1)
pas.grid(row=2,column=1)
b1=Button(text="create db",command=database,padx=50)
b1.grid(row=3,column=1)
b1=Button(text="submit",command=sql,padx=50)
b1.grid(row=4,column=1)

root.geometry("300x200")
root.mainloop()
