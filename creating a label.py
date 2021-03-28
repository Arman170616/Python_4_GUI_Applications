from tkinter import  *


top = Tk()
top.geometry('400x400')

uname=Label(top, text='Username').place(x=30, y = 50)

password=Label(top, text='Password').place(x=30, y = 90)

submitbtn = Button(top, text='submit', activebackground='pink', activeforeground='green').place(x=30, y=120)

e1 = Entry(top, width=20).place(x=100, y=50)
e2 = Entry(top, width=20).place(x=100, y=90)

top.mainloop()