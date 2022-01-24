from tkinter import *

def tut(event):
    print(f"you clicked on the button at {event.x},{event.y}")

root=Tk()
root.title("events in tkinter")
root.geometry("600x300")

widget = Button(root,text="click here")
widget.pack()

widget.bind('<Button-1>',tut)
widget.bind('<Double-1>',quit)

root.mainloop()
