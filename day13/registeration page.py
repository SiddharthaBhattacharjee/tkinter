from tkinter import *

root=Tk()

root.title("Registration page")

def getval():
    print("submitted")
    with open("reg.txt","a") as f:
        f.write((f"name is {nam.get()}\n")),
        f.write((f"Class is {cla.get()}\n")),
        f.write((f"Roll number is {rol.get()}\n")),
        f.write((f"Gender is {gen.get()}\n")),

Name=Label(root,text="Name")
Name.grid(row=1,column=0)

roll_num=Label(root,text="Roll No")
roll_num.grid(row=2,column=0)

Class=Label(root,text="Class")
Class.grid(row=3,column=0)

gender=Label(root,text="Gender")
gender.grid(row=4,column=0)

nameentry=StringVar()
classentry=StringVar()
rollentry=StringVar()
genderentry=StringVar()

nam=Entry(root,textvariable=nameentry)
cla=Entry(root,textvariable=classentry)
rol=Entry(root,textvariable=rollentry)
gen=Entry(root,textvariable=genderentry)

nam.grid(row=1,column=1)
cla.grid(row=3,column=1)
rol.grid(row=2,column=1)
gen.grid(row=4,column=1)

Button(root,text="submit",command=getval).grid(row=6,column=1)

root.geometry("300x200")
root.mainloop()
