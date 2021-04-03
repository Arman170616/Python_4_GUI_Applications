import tkinter
from tkinter import BOTH
#define window
root = tkinter.Tk()
root.title('Label Basic!')
root.geometry('400x400')
root.resizable(0,0)
root.config(bg='green')

#create widget
name_label_1 = tkinter.Label(root, text='hello, my name is arman.')
name_label_1.pack()


name_label_2 = tkinter.Label(root, text='hello, my name is jhon', font=('Arial', 18, 'bold'))
name_label_2.pack()

name_label_3 = tkinter.Label(root, text='hello, my name is paul', font=('Arial', 10), bg='#ff0000')
name_label_3.pack(padx=10, pady=50)

name_label_4 = tkinter.Label(root, text='hello, my name is sue', bg='#000000', fg='yellow')
name_label_4.pack(pady=(0,10), ipadx=50, ipady=10, anchor='e')


name_label_5 = tkinter.Label(root, text='hello, my name is pat', bg='#ffffff', fg='#123456')
name_label_5.pack(fill=BOTH, expand=True)
#Run the root window's main loop
root.mainloop()