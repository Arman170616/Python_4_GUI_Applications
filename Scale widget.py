from tkinter import *  
  
def select():  
   sel = "Value = " + str(v.get())  
   label.config(text = sel)  
     
top = Tk()  
top.geometry("400x400") 

top.title('Scale widget')


v = DoubleVar()  


scale = Scale( top, variable = v, from_ = 1, to = 500, orient = HORIZONTAL)  
scale.pack(anchor=CENTER)  
  
btn = Button(top, text="Value", command=select)  
btn.pack(anchor=CENTER)  
  
label = Label(top)  
label.pack()  
  
top.mainloop() 