from tkinter import *
root=Tk()

def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1
i=0

root.geometry("600x400")
root.title("listbox")

lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"List starts here")

Button(root,text= "Add item", command=add).pack()

root.mainloop()