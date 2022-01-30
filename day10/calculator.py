from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text =="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update()

    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root=Tk()
root.geometry("644x800")
root.title("my calulator")
root.wm_iconbitmap("1.ico")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue,font="cursive 40 bold")
screen.pack(fill=X, ipadx=8, pady=10,padx=10)

f=Frame(root,bg="grey")
b=Button(f,text="9",padx=25, pady=12, font="cursive 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="8",padx=25, pady=12, font="cursive 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="7",padx=25, pady=12, font="cursive 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="6",padx=25, pady=12, font="cursive 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="5",padx=25, pady=12, font="cursive 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="4",padx=25, pady=12, font="cursive 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="0",padx=29, pady=12, font="cursive 35 bold")
b.pack(side=LEFT,padx=17,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="-",padx=29, pady=12, font="cursive 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="/",padx=29, pady=12, font="cursive 35 bold")
b.pack(side=LEFT,padx=19,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="%",padx=23, pady=12, font="cursive 35 bold")
b.pack(side=LEFT,padx=19,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="+",padx=23, pady=12, font="cursive 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="*",padx=23, pady=12, font="cursive 35 bold")
b.pack(side=LEFT,padx=19,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f,text=".",padx=27, pady=12, font="cursive 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="=",padx=26, pady=12, font="cursive 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="C",padx=25, pady=12, font="cursive 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

root.mainloop()