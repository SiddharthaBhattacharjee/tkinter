from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry("600x300")
root.title("sliders")

def get_age():
    print(f"the age is {myslider2.get()}")
    msg.showinfo("thanks for submitted your age","we have recorded your response")

#myslider= Scale(root, from_=0,to=100)
#myslider.pack()

Label(root,text="tell your age").pack()
myslider2= Scale(root, from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
myslider2.set(18)
myslider2.pack()

button= Button(root,text="submit",command=get_age).pack()

root.mainloop()