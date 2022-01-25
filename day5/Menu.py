from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("600x400")
root.title("menu")

def myfunc():
    print("my menu")

def help():
    print("I'll help you")
    a = tmsg.showinfo("Help","will get back to you soon")
    print(a)

def rate():
    print("rate us ")
    a= tmsg.askquestion("Rate us","how was your experience?")
    if a == "yes":
        msg="rate us on app store"
    else:
        msg="tell us what's wrong? we'll get back to you soon."
    tmsg.showinfo("experience",msg)

yourmenu=Menu(root)
m1=Menu(yourmenu,tearoff=0)
m1.add_command(label="New item",command=myfunc)
m1.add_command(label="save",command=myfunc)
m1.add_separator()
m1.add_command(label="save as",command=myfunc)
m1.add_command(label="exit",command=quit)
yourmenu.add_cascade(label="file",menu=m1)

m2=Menu(yourmenu,tearoff=0)
m2.add_command(label="cut",command=myfunc)
m2.add_command(label="save",command=myfunc)
m2.add_separator()
m2.add_command(label="rate us",command=rate)
yourmenu.add_cascade(label="edit",menu=m2)

m3= Menu(yourmenu,tearoff=0)
m3.add_command(label="help",command=help)
yourmenu.add_cascade(label="help",menu=m3)
root.config(menu=yourmenu)

root.mainloop()