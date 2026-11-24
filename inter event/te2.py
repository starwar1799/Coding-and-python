from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

def msg():
    messagebox.askyesno("Very real and accurate virus checker", "Do you want to delete the virus")

button = Button(root, text = "ooh look its a virus :O :O", command=msg)
button.place(x=40, y=80)

root.mainloop()