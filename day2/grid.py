import sys
from tkinter import *

var=Tk()
var.geometry("600x340")

def getvals():
    print(f"the username is {uservalue.get()}")
    print(f"the password is {passvalue.get()}")

def exit():
    sys.exit()

username=Label(var,text="Username")
password=Label(var,text="Password")
username.grid()
password.grid()

uservalue=StringVar()
passvalue=StringVar()

uservalue=Entry(var,textvariable=uservalue)
passvalue=Entry(var,textvariable=passvalue)

uservalue.grid(row=0,column=1)
passvalue.grid(row=1,column=1)

Button(text="submit", command=getvals).grid()
Button(text="exit", command=exit).grid(row=2,column=2)

var.mainloop()
