import tkinter as tk
from tkinter import ttk

cal = tk.Tk()
#title
cal.title('calculator')
#windowsize
cal.geometry('1080x200')
cal.maxsize(width=1080, height=200)
cal.minsize(width=1080, height=200)
cal.configure(bg='cyan')


#entry box
equation = tk.IntVar()
ds_entry = ttk.Entry(cal,state = 'readonly', textvariable = equation)
ds_entry.grid(row=1, column = 0, ipadx = 20, ipady=20)

equatio = tk.IntVar()
dsentry = ttk.Entry(cal,state = 'readonly', textvariable = equatio)
dsentry.grid(row=1, column = 1, ipadx = 20, ipady=20)

equati = tk.StringVar()
dentry = ttk.Entry(cal,state = 'readonly', textvariable = equati)
dentry.grid(row=1, column = 2, ipadx = 20, ipady=20)



exp = " "
def press(num):
    global exp
    exp = exp + str(num)
    equation.set(exp)


def clear():
    global exp
    global ex
    global e
    exp = ""
    ex = ""
    e = ""
    equation.set("")
    equatio.set("")
    equati.set("")
    


ex = " "
def pres(num):
    global ex
    ex = ex + str(num)
    equatio.set(ex)

e = " "
def prss(num):
    global e
    e = equation.get() + equatio.get() 
    equati.set(e)

s = ""
def sub(num):
    global s
    s = equation.get() - equatio.get() 
    equati.set(s)

m = ""
def multi(num):
    global m
    m = equation.get() * equatio.get() 
    equati.set(m)

d = ""
def div(num):
    global d
    d = equation.get() / equatio.get() 
    equati.set(d)


#first
one = ttk.Button(cal,text='1', width=6, command = lambda : press('1'))
one.grid(row = 1, column = 3, ipadx = 6, ipady = 10)

two = ttk.Button(cal,text='2', width=6, command = lambda : press('2'))
two.grid(row = 1, column = 4, ipadx = 6, ipady = 10)

three = ttk.Button(cal,text='3', width=6, command = lambda : press('3'))
three.grid(row = 1, column = 5, ipadx = 6, ipady = 10)

four = ttk.Button(cal,text='4', width=6, command = lambda : press('4'))
four.grid(row = 1, column = 6, ipadx = 6, ipady = 10)

five = ttk.Button(cal,text='5', width=6, command = lambda : press('5'))
five.grid(row = 1, column = 7, ipadx = 6, ipady = 10)

six = ttk.Button(cal,text='6', width=6, command = lambda : press('6'))
six.grid(row = 1, column = 8, ipadx = 6, ipady = 10)

seven = ttk.Button(cal,text='7', width=6, command = lambda : press('7'))
seven.grid(row = 1, column = 9, ipadx = 6, ipady = 10)

eight = ttk.Button(cal,text='8', width=6, command = lambda : press('8'))
eight.grid(row = 1, column = 10, ipadx = 6, ipady = 10)

nine = ttk.Button(cal,text='9', width=6, command = lambda : press('9'))
nine.grid(row = 1, column = 11, ipadx = 6, ipady = 10)

zero = ttk.Button(cal,text='0', width=6, command = lambda : press('0'))
zero.grid(row = 1, column = 12, ipadx = 6, ipady = 10)
#second
one= ttk.Button(cal,text='1', width=6, command = lambda : pres('1'))
one.grid(row = 2, column = 3, ipadx = 6, ipady = 10)

two= ttk.Button(cal,text='2', width=6, command = lambda : pres('2'))
two.grid(row = 2, column = 4, ipadx = 6, ipady = 10)

three= ttk.Button(cal,text='3', width=6, command = lambda : pres('3'))
three.grid(row = 2, column = 5, ipadx = 6, ipady = 10)

four= ttk.Button(cal,text='4', width=6, command = lambda : pres('4'))
four.grid(row = 2, column = 6, ipadx = 6, ipady = 10)

five= ttk.Button(cal,text='5', width=6, command = lambda : pres('5'))
five.grid(row = 2, column = 7, ipadx = 6, ipady = 10)

six= ttk.Button(cal,text='6', width=6, command = lambda : pres('6'))
six.grid(row = 2, column = 8, ipadx = 6, ipady = 10)

seven= ttk.Button(cal,text='7', width=6, command = lambda : pres('7'))
seven.grid(row = 2, column = 9, ipadx = 6, ipady = 10)

eight= ttk.Button(cal,text='8', width=6, command = lambda : pres('8'))
eight.grid(row = 2, column = 10, ipadx = 6, ipady = 10)

nine= ttk.Button(cal,text='9', width=6, command = lambda : pres('9'))
nine.grid(row = 2, column = 11, ipadx = 6, ipady = 10)

zero= ttk.Button(cal,text='0', width=6, command = lambda : pres('0'))
zero.grid(row = 2, column = 12, ipadx = 6, ipady = 10)


#addition
add = ttk.Button(cal,text='+', width=6, command = lambda : prss('+'))
add.grid(row = 5, column = 3, ipadx = 6, ipady = 10)

#substraction

minus = ttk.Button(cal,text='-', width=6, command = lambda : sub('-'))
minus.grid(row = 5, column = 4, ipadx = 6, ipady = 10)

#multiplication
into = ttk.Button(cal,text='*', width=6, command = lambda : multi('*'))
into.grid(row = 5, column = 5, ipadx = 6, ipady = 10)

#divide
minus = ttk.Button(cal,text='/', width=6, command = lambda : div('/'))
minus.grid(row = 5, column = 6, ipadx = 6, ipady = 10)



clea = ttk.Button(cal,text='clear', width=6, command = clear)
clea.grid(row = 5, column = 7, ipadx = 6, ipady = 10)
cal.mainloop()