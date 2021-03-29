from tkinter import *

def selection():
    selection = "you selected the option " + str(radio.get())
    label.config(text=selection)


top=Tk()
top.geometry('300x300')

radio = IntVar()
lbl = Label(text = "Favourite Programming Language: ")
lbl.pack()

R1 = Radiobutton(top, text='C', variable=radio, value=1, command=selection)
R1.pack(anchor= W)

R2 = Radiobutton(top, text='C++', variable=radio, value=2, command=selection)
R2.pack(anchor= W)


R3 = Radiobutton(top, text='C#', variable=radio, value=3, command=selection)
R3.pack(anchor= W)


label = Label(top)
label.pack()

top.mainloop()