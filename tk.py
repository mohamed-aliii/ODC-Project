from tkinter import *
import datetime
def submit():
    label2["text"]=datetime.datetime.now().year-int(entry1.get())
    entry1.delete(0,END)
def exit():
    win.destroy()
def search():
    name=entry2.get().capitalize()
    with open(r"C:\Users\DELL\OneDrive - Alexandria National University\Desktop\Students.txt","r+") as file:
        content=file.read()
        if name in content:
            label4["text"]="Student found"
            label4["fb"]="green"
        else:
            label4["text"]="Student not found\n The name is registered"
            label4["fg"]="red"
            file.write("\n"+name)


win=Tk()
win.geometry("620x700")
win.title("ODC")
win.config(bg="lavenderblush3")
label1=Label(win,text="Enter your age :",bg="lavenderblush4",font=("aria",20))
label1.place(x=10,y=20,height=40,width=600)

entry1=Entry(win)
entry1.place(x=10,y=80,height=40,width=600)

button1=Button(win,text="Get the born year",bg="lavenderblush4",font=("aria",15),command=submit)
button1.place(x=10,y=140,height=40,width=600)

label2=Label(win,text="",bg="lavenderblush3",font=("aria",25))
label2.place(x=10,y=220,height=40,width=600)

label3=Label(win,text="Enter Your First Name :",bg="lavenderblush4",font=("aria",20))
label3.place(x=10,y=280,height=40,width=600)

entry2=Entry(win)
entry2.place(x=10,y=340,height=40,width=600)

button3=Button(win,text="Search",bg="lavenderblush4",font=("aria",15),command=search)
button3.place(x=10,y=400,height=40,width=600)

button4=Button(win,text="Exit",bg="lavenderblush4",font=("aria",15),command=exit)
button4.place(x=10,y=460,height=40,width=600)

label4=Label(win,text="",bg="lavenderblush3",font=("aria",25))
label4.place(x=10,y=520,height=100,width=600)
win.mainloop()