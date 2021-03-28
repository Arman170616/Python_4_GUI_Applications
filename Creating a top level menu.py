from tkinter import  *

top = Tk()
def hello():
    print('hey bro!')

menubar = Menu(top)

menubar.add_command(label='Hello', command=hello)
menubar.add_command(label='Quit', command=exit)
top.config(menu=menubar)

top.mainloop()