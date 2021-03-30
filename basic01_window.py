# #import tkinter
# from tkinter import *

# # root = Tk()
# # root.title('Window basics!')
# # root.iconbitmap('Google-Noto-Emoji-Smileys-10024-thinking-face.ico')  #/home/pyarena/python/GUI/pyarena tu/Coffee.ico

# root = Tk()
# img = PhotoImage(file='Google-Noto-Emoji-Smileys-10024-thinking-face.ico')
# root.tk.call('wm', 'iconphoto', root._w, img)

# root.mainloop()

import os
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("My Application")
if "nt" == os.name:
    root.wm_iconbitmap(bitmap = "myicon.ico")
else:
    root.wm_iconbitmap(bitmap = "@myicon.xbm")

root.mainloop()