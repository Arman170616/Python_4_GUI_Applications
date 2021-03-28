from tkinter import *

top =Tk()
top.geometry('400x400')


label = Label(top, text= 'A list of favourite countries..')

listbox = Listbox(top)
listbox.insert(1,'Bangladesh')
listbox.insert(2, 'Pakistan')
listbox.insert(3, 'india')
listbox.insert(4, "Japan")  
listbox.insert(5, "Austrelia") 

label.pack()
listbox.pack()


top.mainloop()