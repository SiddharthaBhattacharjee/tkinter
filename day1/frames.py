from tkinter import *
root= Tk()
root.geometry("800x400")
f1=Frame(root,bg="grey", borderwidth=8,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")

f2 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
f2.pack(side=TOP, fill=X)

l = Label(f1,text="left frame",font="cursive",fg="red")
l.pack(pady=160)
l = Label(f2,text="top frame",font="cursive",fg="red")
l.pack()

root.mainloop()