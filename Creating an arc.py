from tkinter import  *

top = Tk()
top.geometry('200x300')

c = Canvas(top, bg='yellow', height='300')
arc = c.create_arc((5,10,150,200),start = 0,extent = 150, fill= "pink")

c.place()

top.mainloop()