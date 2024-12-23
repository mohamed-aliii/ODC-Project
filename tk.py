from tkinter import *
import datetime
def submit():
    label2["text"]=datetime.datetime.now().year-int(entry1.get())
    entry1.delete(0,END)
def exit():
    win.destroy()
win=Tk()
win.geometry("620x600")
win.title("ODC")
win.config(bg="lavenderblush3")
label1=Label(win,text="Enter your age :",bg="lavenderblush4",font=("aria",20))
label1.place(x=10,y=20,height=40,width=600)
entry1=Entry(win)
entry1.place(x=10,y=80,height=40,width=600)
button1=Button(win,text="Get the born year",bg="lavenderblush4",font=("aria",15),command=submit)
button1.place(x=10,y=140,height=40,width=600)
button1=Button(win,text="Exit",bg="lavenderblush4",font=("aria",15),command=exit)
button1.place(x=10,y=200,height=40,width=600)
label2=Label(win,text="",bg="lavenderblush3",font=("aria",25))
label2.place(x=10,y=260,height=40,width=600)
win.mainloop()