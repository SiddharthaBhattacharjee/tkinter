import sys
from tkinter import *
srt=Tk()
srt.geometry("600x340")

def hello():
    print("hello!!!")

def name():
    print("My name is Arnav")

def view():
    from PIL import Image
    img=Image.open("photo.jfif")
    img.show()
    img.save("photo.jpg")
def exit():
    sys.exit()

frame = Frame(srt,bg="red", borderwidth=3,relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1= Button(frame,text="hey",fg="red",bg="black",command=hello)
b1.pack(side=LEFT)
b2= Button(frame,text="Name",fg="red",bg="black",command=name)
b2.pack(side=LEFT)
b3= Button(frame,text="View image",fg="red",bg="black",command=view)
b3.pack(side=LEFT)
b4= Button(frame,text="exit",fg="red",bg="black",command=exit)
b4.pack(side=LEFT)

srt.mainloop()
