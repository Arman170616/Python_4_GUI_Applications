from tkinter import *
import pyttsx3


top = Tk()
top.title('tkinter window')
top.geometry('800x500')
top.config(bg='#123456')

def talk():
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)  #setting up new voice rate
    #voices = engine.getProperty('voices')
    #engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female
    engine.say(my_entry.get())
    
    #engine.save_to_file('Hello World', 'test1.mp3')
    engine.runAndWait()
    my_entry.delete(0,END)



my_entry = Entry(top, font=('Lora', 15))
my_entry.pack(pady=20)
my_button = Button(top, text='push', command=talk)
my_button.pack(pady=20)

top.mainloop()