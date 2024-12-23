from tkinter import *
import datetime

def exit():
    win.destroy()
def search():
    name=entry1.get().capitalize()
    with open(r"C:\Users\DELL\OneDrive - Alexandria National University\Desktop\Students.txt","r+") as file:
        content=file.read()
        if name in content:
            label2["text"]="Student found"
            label2["fb"]="green"
        else:
            label2["text"]="Student not found\n The name is registered"
            label2["fg"]="red"
            file.write("\n"+name)
win=Tk()
win.geometry("620x700")
win.title("Boycott Brands")
#win.config(bg="lavenderblush3")

label1=Label(win,text="Enter your age :")
label1.place(x=10,y=20,)

entry1=Entry(win)
entry1.place(x=10,y=80)

button1=Button(win,text="Get the born year",command=search)
button1.place(x=10,y=140)

label2=Label(win,text="",)
label2.place(x=10,y=220,)
win.mainloop()