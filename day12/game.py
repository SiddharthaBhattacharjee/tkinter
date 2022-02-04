import tkinter
from tkinter import *
import random
colors=['Red','Pink','Blue','Yellow','Orange','White','Purple','Brown']
run=0
timeout=20
with open("Highscore.txt",'r') as Hs:
    highscore = Hs.read()
    highscore = int(highscore)
def stgame(event):
    if timeout==20:
        countdown()
    nextcolour()
def nextcolour():
    global run
    global timeout
    global highscore
    if timeout>0:
        e.focus_set()
        if e.get().lower()==colors[1].lower():
            run+=1
            if run > highscore:
                highscore = run
        e.delete(0,tkinter.END)
        random.shuffle(colors)
        label.config(fg=str(colors[1]),text=str(colors[0]))
        a.config(text="score : "+str(run))
        a1.config(text="Highscore : "+str(highscore))

def countdown():
    global timeout
    global highscore
    if timeout>0:
        timeout-=1
        b.config(text="Time Left:"+str(timeout))
        b.after(1000,countdown)
    else:
        with open("Highscore.txt",'w') as Hs:
            Hs.write(str(highscore))

def gg():
    if timeout==20:
        countdown()
    nextcolour()

def reset():
    global run
    global timeout
    timeout=20
    run=0
    nextcolour()

root=Tk()

root.geometry("600x400")
root.title("game")

label= Label(root,text="enter the text colour not the text",font="cusrsive 20 bold")
label.pack()

a=Label(root,text="press start to enter",font=("cursive 13 "))
a.pack()

a1=Label(root,text="Highscore : "+str(highscore),font=("cursive 13 "))
a1.pack()

b=Label(root,text="time left: "+str(timeout),font=("cursive 13"))
b.pack()

c=Label(root,font="cursive 20")
c.pack()

e=Entry(root)
root.bind("<Return>",stgame)
e.pack()
e.focus_set()

b1 = Button(root,text="Start",fg="blue",command=gg)
b1.pack()

b2 = Button(root,text="Reset",fg="blue",command=reset)
b2.pack()

root.mainloop()
