from tkinter import *

def update():
    print("resizing the gui")
    root.geometry(f"{width.get()}x{height.get()}")

root= Tk()
root.geometry("400x300")

root.title("Window Resizer" )
Label(root,text = "Window Resizer " , font = "comicsansms 11 bold ", fg = "red", pady = 20).pack()


width=StringVar()
height=StringVar()

Entry(root,textvariable=width).pack()
Entry(root,textvariable=height).pack()
Button(root,text="apply",command=update).pack()

root.mainloop()