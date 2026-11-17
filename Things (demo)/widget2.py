from tkinter import *
from datetime import date

root = Tk()
root.title('widegt starting thingy')
root.geometry('400x400')

lbl = Label(text= "hi.", fg="white", bg="#072F5F", height=1, width=300)

name_lbl = Label(text="Full Name", bg="#3895D3")
name_entry = Entry()

def display():
    name = name_entry.get()
    global Message
    message = "This the application. \n Today date ="
    greet = "Hi"+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3)

btn = Button(text="start", command=display, height=1, bg="#1261A0", fg='white')

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()