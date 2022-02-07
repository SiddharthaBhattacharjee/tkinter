from tkinter import *
import tkinter.messagebox as msg
import mysql.connector as mysql

root=Tk()

def database():
    USer = user.get()
    PASSword = pas.get()
    b=mysql.connect(host="localhost",user="root", password="123456",database="registeration")
    cursor=b.cursor()
    a= b.cursor()
    cursor.execute("select password,username from info;")

    for(username,password) in cursor:
        if username == USer and password == PASSword:
            print("login successful")
        else:
            print("username or password is invalid")
    a.close()
    b.close()

username=Label(root,text="Username",font="cursive 13 bold")
username.grid(row=0,column=0)

password=Label(root,text="Password",font="cursive 13 bold")
password.grid(row=2,column=0)

userval=StringVar()
passval=StringVar()

user=Entry(root,textvariable=userval)
pas=Entry(root,textvariable=passval)
user.grid(row=0,column=1)
pas.grid(row=2,column=1)
b1=Button(text="submit",command=database,padx=50)
b1.grid(row=3,column=1)

root.geometry("300x200")
root.mainloop()