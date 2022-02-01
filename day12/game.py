import tkinter
from tkinter import *
import random
colors=['Red','Pink','Blue','Yellow','Orange','White','Purple','Brown']
run=0
timeout=20
def stgame(event):
    if timeout==20:
        countdown()
    nextcolour()
def nextcolour():
    global run
    global timeout
    if timeout>0:
        e.focus_set()
        if e.get().lower()==colors[1].lower():
            run+=1
        e.delete(0,tkinter.END)
        random.shuffle(colors)
        label.config(fg=str(colors[1]),text=str(colors[0]))
        a.config(text="score:-"+str(run))

def countdown():
    global timeout
    if timeout>0:
        timeout-=1
        b.config(text="Time Left:"+str(timeout))
        b.after(1000,countdown)

root=Tk()

root.geometry("600x400")
root.title("game")

label= Label(root,text="enter the text colour not the text",font="cusrsive 20 bold")
label.pack()

a=Label(root,text="press start to enter",font=("cursive 13 "))
a.pack()

b=Label(root,text="time left:- "+str(timeout),font=("cursive 13"))
b.pack()

c=Label(root,font="cursive 20")
c.pack()

e=Entry(root)
root.bind("<Return>",stgame)
e.pack()
e.focus_set()

root.mainloop()