from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file=None
    textarea.delete(1.0,END)
    
def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("all files","*.*"),("text documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"- Notepad")
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()
def savefile():
    global file
    if file == None:
        file=askopenfilename(defaultextension=".txt",filetypes=[("all files","*.*"),("text documents","*.txt")])
        if file == "":
            file=None
        else:
            f=open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+("- Notepad"))
    else:
        f=open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()

def quitapp():
    root.destroy()
def cut():
    textarea.event_generate(("<<Cut>>"))
def copy():
    textarea.event_generate(("<<Copy>>"))
def paste():
    textarea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad","Notepad by Arnav kaushik")

if __name__ =='__main__':
    root=Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("1.ico")
    root.geometry("600x400")

    #adding text area
    textarea=Text(root,font="cursive 13")
    textarea.pack(expand=TRUE,fill=BOTH)
    file= None

    #creating menubar
    Menubar=Menu(root)
#creating filemenu starts here
    FileMenu=Menu(Menubar,tearoff=0)

    #to open new file
    FileMenu.add_command(label="New",command=newFile)

    #to open already existing file
    FileMenu.add_command(label="open",command=openfile)

    #to save a current file
    FileMenu.add_command(label="save",command=savefile)
    FileMenu.add_separator()
    FileMenu.add_command(label="exit",command=quitapp)
    Menubar.add_cascade(label="file",menu=FileMenu)
# creating filemenu ends

#edit menu creating starts here
    Editmenu=Menu(Menubar,tearoff=0)
    #adding cut feature
    Editmenu.add_command(label="cut",command=cut)
    Editmenu.add_command(label="copy",command=copy)
    Editmenu.add_command(label="paste",command=paste)

    Menubar.add_cascade(label="Edit",menu=Editmenu)
#edit menu creating ends here

#help menu creating starts here
    Helpmenu=Menu(Menubar,tearoff=0)
    Helpmenu.add_command(label="About Notepad",command=about)
    Menubar.add_cascade(label="help",menu=Helpmenu)
#help menu creating ends here

    root.config(menu=Menubar)
#adding scrollbar
    scroll=Scrollbar(textarea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=scroll.set)
    root.mainloop()
