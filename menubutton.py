from tkinter import *

top = Tk()

top.geometry('400x400')

menubutton = Menubutton(top, text='Language', relief=RAISED)
menubutton.grid()

menubutton.menu = Menu(menubutton)
menubutton["menu"]=menubutton.menu  

menubutton.menu.add_checkbutton(label='Bangla', variable=IntVar())
menubutton.menu.add_checkbutton(label='English', variable=IntVar())
menubutton.menu.add_checkbutton(label='shuomi', variable=IntVar())
menubutton.menu.add_checkbutton(label='German', variable=IntVar())

menubutton.pack()
top.mainloop()