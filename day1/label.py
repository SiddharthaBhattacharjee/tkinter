from tkinter import *

root = Tk()
root.geometry("444x253")
root.title("get a new label to my gui")

title_label = Label(text = '''here goes the text for our gui label''', bg="red", fg="black",padx = 140, pady= 90, font=("cursive",10, "bold "), borderwidth=5,relief=SUNKEN)


title_label.pack()
root.mainloop()
