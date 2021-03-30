from tkinter import *

top =Tk()
top.geometry('400x400')
top.title('grid method widget')

name = Label(top, text='Name').grid(row=0, column=0)
e1 = Entry(top).grid(row=0, column=1)

password = Label(top, text='password').grid(row=1, column=0)
e2 = Entry(top).grid(row=1, column=1)

submit = Button(top, text='submit').grid(row=4, column=0)

top.mainloop()