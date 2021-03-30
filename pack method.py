from tkinter import *

top  = Tk()

top.geometry("200x200")
top.title("pack widget")


redbutton = Button(top, text='Red', fg='red')
redbutton.pack(side=LEFT)

greenbutton = Button(top, text='Green', fg='green')
greenbutton.pack(side=RIGHT)

blackbutton = Button(top, text='Black', fg='Black')
blackbutton.pack(side=TOP)

bluebutton = Button(top, text='Blue', fg='blue')
bluebutton.pack(side=BOTTOM)

top.mainloop()