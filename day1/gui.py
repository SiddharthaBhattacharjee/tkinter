from tkinter import *
from PIL import Image, ImageTk

new_root = Tk()
new_root.geometry("644x434")

image = Image.open("photo.jpg")

photo = ImageTk.PhotoImage(image)
new_label = Label(image=photo)

new_label.pack(fill = X)


new_root.mainloop()
