from tkinter import *
 

top = Tk()

top.geometry('400x400')

chrvar1 = IntVar()
chrvar2 = IntVar()
chrvar3 = IntVar()


chrbtn1 = Checkbutton(top, text='C', variable = chrvar1, onvalue=1, offvalue=0, height=2, width=10)

chrbtn2 = Checkbutton(top, text='java', variable = chrvar2, onvalue=1, offvalue=0, height=2, width=10)

chrbtn3 = Checkbutton(top, text='python', variable = chrvar3, onvalue=1, offvalue=0, height=2, width=10)

chrbtn1.pack()
chrbtn2.pack()
chrbtn3.pack()


top.mainloop()