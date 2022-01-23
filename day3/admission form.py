from tkinter import *
root=Tk()
root.geometry("600x400")

#to get values from the gui
def getval():
    print("Your response have been taken" )
    print(f"name is {Nameentry.get()}")
    print(f"Gender is {Genderentry.get()}")
    print(f"phone number is {Phone_numberentry.get()}")
    print(f"Address is {Addressentry.get()}")
    print(f"Details of hostel {var1.get()}")
    
#to enter the values in a txt file
    with open("records.txt","a") as f:
        f.write((f"name is {Nameentry.get()}\n")),
        f.write((f"Gender is {Genderentry.get()}\n")),
        f.write((f"phone number is {Phone_numberentry.get()}\n")),
        f.write((f"Address is {Addressentry.get()}\n")),
        f.write((f"Details of hostel {var1.get()}\n")),



#defining emty variable to get results from checkbox
var1=IntVar()

#Text in the form
Label(root,text="welcome to admission portal",font="cursive 12 bold").grid(row=0,column=3)

Name=Label(root,text="Name")
Gender=Label(root,text="Gender")
Phone_number=Label(root,text="phone number")
Address=Label(root,text="Address")

Name.grid(row=2,column=0)
Gender.grid(row=3,column=0)
Phone_number.grid(row=4,column=0)
Address.grid(row=5,column=0)

#Defining variables for storing values
Namevalue = StringVar()
Gendervalue = StringVar()
Phone_numbervalue = StringVar()
Addressvalue = StringVar()
hostelvalue = IntVar()

#entries for our form
Nameentry= Entry(root, textvariable=Namevalue)
Genderentry= Entry(root, textvariable=Gendervalue)
Phone_numberentry= Entry(root, textvariable=Phone_numbervalue)
Addressentry= Entry(root, textvariable=Addressvalue)

#packing of entries
Nameentry.grid(row=2, column=3)
Genderentry.grid(row=3, column=3)
Phone_numberentry.grid(row=4, column=3)
Addressentry.grid(row=5, column=3)

#checkbox
hostel = Checkbutton(text="do you want hostel ?",variable=var1,onvalue=1, offvalue=0,)
hostel.grid(row=6, column=3)

#submit button
Button(text="submit",command=getval).grid(row=7, column=3)

root.mainloop()
