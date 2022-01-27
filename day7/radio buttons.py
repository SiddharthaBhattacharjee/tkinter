from tkinter import *
import tkinter.messagebox as msg
root=Tk()

root.geometry("600x400")
root.title("radio buttons")

def colour():
    msg.showinfo("your response have been taken!", f"thanks for submitting your response your chosen colour is {var.get()} ")
    print("chosen color is",var.get())

var=StringVar()
var.set("Radio")

#var= IntVar()

Label(root,text="which is your favourite color?",font="cursive 19 bold",justify=LEFT,padx=14).pack()
radio=Radiobutton(root,text="red",padx=14,variable=var,value="red").pack(anchor="w")
radio=Radiobutton(root,text="blue",padx=14,variable=var,value="blue").pack(anchor="w")
radio=Radiobutton(root,text="green",padx=14,variable=var,value="green").pack(anchor="w")
radio=Radiobutton(root,text="black",padx=14,variable=var,value="black").pack(anchor="w")

Button(root,text="submit",command=colour).pack()

root.mainloop()