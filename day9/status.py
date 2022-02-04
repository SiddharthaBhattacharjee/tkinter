from tkinter import *

def upload():
    sta.set("Uploading...")
    sbar.update()
    import time
    time.sleep(2)
    sta.set("Uploading complete")

root=Tk()
root.geometry("600x300")
root.title("creating status bar")

sta=StringVar()
sta.set("ready")

sbar=Label(root,textvariable=sta,relief=SUNKEN,anchor="w")
sbar.pack(side=BOTTOM,fill=X)
Button(root,text="upload",command=upload).pack()

root.mainloop()