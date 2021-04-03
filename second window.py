import tkinter

#Define window
root = tkinter.Tk()
root.title('first window ')
root.geometry('200x300')
#root.iconbitmap(icon)
root.config(bg='#123556')
root.resizable(0,0)

#second window
top =tkinter.Toplevel()
top.title('Second window')
top.config(bg="#123456")
top.geometry('200x350+500+50')

#run root window's main loop
root.mainloop()