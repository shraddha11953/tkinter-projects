import tkinter as tk
from tkinter import ttk
from tkinter import *

project = tk.Tk()


project.geometry('1000x400')
project.maxsize(width=1000, height=400)
project.minsize(width=1000, height=400)
project.configure(bg='cyan')
var = IntVar()
vark = tk.StringVar()
ds_entry = ttk.Entry(project,state = 'readonly', textvariable = Text)
ds_entry.grid(row=2, column=0, ipadx = 20, ipady=20)
def prss(var):
    if var == str(1) :
        print("you win ")
    
que1 = Label(project,text="who is the pm of india  : ",height= 3, width= 20)
que1.grid(row=1,column=0)
radio = Radiobutton(project,text="narendra modi",variable=var,value=1,height=3,width=20)
radio.grid(row=1,column=1)
radio = Radiobutton(project,text="eknath shinde",variable=var,value=2,height=3,width=20)
radio.grid(row=1,column=2)
radio = Radiobutton(project,text="bg",variable=var,value=3,height=3,width=20)
radio.grid(row=1,column=3)
radio = Radiobutton(project,text="yc",variable=var,value=4,height=3,width=20)
radio.grid(row=1,column=4)
btn = Button(project,text="submit",bg="green",command = lambda : prss('submit'))
btn.grid(row=1,column=5)
project.mainloop()