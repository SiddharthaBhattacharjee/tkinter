from tkinter import *
root=Tk()

root.geometry("600x400")
root.title("scroll bar")

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

listbox= Listbox(root,yscrollcommand=scrollbar.set)
for i in range (344):
    listbox.insert(END,f"item{i}")
listbox.pack(fill="both",padx=22)
scrollbar.config(command=listbox.yview)

root.mainloop()