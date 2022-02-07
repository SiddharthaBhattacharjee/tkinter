from tkinter import *

root=Tk()
root.title("Login")

def getval():
    print("submitted")
    with open("login.txt","a") as f:
        f.write((f"Username is {user.get()}\n")),
        f.write((f"password is {pas.get()}\n")),

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
b1=Button(text="submit",command=getval,padx=50)
b1.grid(row=3,column=1)

root.geometry("300x200")
root.mainloop()
