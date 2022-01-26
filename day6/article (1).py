from tkinter import *
from PIL import ImageTk , Image

def every_100(text):
    final_text =""
    for i in range (0,len(text)):
        final_text += text[i]
        if i%150==0 and i!=0:
            final_text +="\n"
    return final_text

root = Tk()

root.geometry("1000x800")
root.title("Magzine")
root.minsize(200, 100)

texts = []
photos = []
for i in range(0, 3):
    with open(f"{i + 1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f"{i+1}.png")
    image=image.resize((500,200),Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root,width=800,height=70).pack()
Label(f0, text="Articles",font="cursive 33 bold").pack()
Label(f0, text="26th january, 2022 ",font="cursive 10 bold").pack()

f1=Frame(root,width=900,height=200)
Label(f1,text=texts[0],font="cursive 12",padx=22,pady=22).pack(side="left")
Label(f1,image=photos[0],anchor="e").pack(side="right")
f1.pack(anchor="w")

f2=Frame(root,width=900,height=200)
Label(f2,text=texts[1],font="cursive 12",padx=22,pady=22).pack(side="left")
Label(f2,image=photos[1],anchor="e").pack(side="right")
f2.pack(anchor="w")

f3=Frame(root,width=900,height=200)
Label(f3,text=texts[2],font="cursive 12",padx=22,pady=22).pack(side="left")
Label(f3,image=photos[2],anchor="e").pack(side="right")
f3.pack(anchor="w")

root.mainloop()