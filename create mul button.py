from tkinter import *
from tkinter import messagebox

top = Tk()

top.geometry('300x300')

def fun():
    messagebox.showinfo('hello', 'Red button clicked!')
    #showinfo(title="About", message="My Window")

def fun1():
    messagebox.showinfo('danke', 'blue button clicked!')

b1 = Button(top, text="Red", command=fun, activeforeground='red', activebackground='pink', pady=10, padx=15)
b2 = Button(top, text="Blue",command=fun1,  activeforeground='blue', activebackground='pink', pady=10, padx=15)
b3 = Button(top, text="Green",  activeforeground='green', activebackground='pink', pady=10, padx=15)
b4 = Button(top, text="Yellow",  activeforeground='yellow', activebackground='pink', pady=10, padx=15)


b1.pack(side=LEFT)
b2.pack(side=RIGHT)
b3.pack(side=TOP)
b4.pack(side=BOTTOM)

top.mainloop()