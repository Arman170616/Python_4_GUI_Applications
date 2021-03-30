from tkinter import *
import pyttsx3


root = Tk()
root.title('Text to Speech')
root.geometry('400x400')
#root.iconbitmap(r'Coffee.ico')

engine = pyttsx3.init()
engine.say('hello arman')
engine.runAndWait()

root.mainloop()