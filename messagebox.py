from tkinter import *
from tkinter.messagebox import showinfo


def callAbout():
    showinfo(title="About", message="My Window")


win = Tk()

win.geometry('300x300')
win.title("My First Window")

bar_menu = Menu(win)

menu_about = Menu(bar_menu, tearoff=0)
bar_menu.add_cascade(label="About", menu=menu_about)
menu_about.add_command(label="About", command=callAbout)

win.config(menu=bar_menu)

win.mainloop()