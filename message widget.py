from tkinter import *

top = Tk()

top.title('Tkinter Message')
top.geometry("300x300")  
#var = StringVar()  
message = Message(top, text='welcome to the message widget')
message.pack()
top.mainloop()