import tkinter


#Define window
root = tkinter.Tk()
root.title('morse code tanslator')
root.geometry('500x350')
#root.iconbitmap('Icons8-Ios7-Industry-Radio-Tower.ico')
root.resizable(0,0)


#define fonts colors
button_font = ('SimSun', 10)
root_color = '#778899'
frame_color = '#dcdcdc'
button_color= '#c0c0c0'
text_color = '#f8f8ff'
root.config(bg=root_color)

#define function

#Create our morse code dictionaries
english_to_morse = {
    'a': '.-', 
    'b': '-...', 
    'c': '-.-.', 
    'd': '-..',
    'e': '.', 
    'f': '..-.', 
    'g': '--.', 
    'h': '....',
    'i': '..', 
    'j': '.---', 
    'k': '-.-', 
    'l': '.-..',
    'm': '--', 
    'n': '-.', 
    'o': '---', 
    'p': '.--.',
    'q': '--.-', 
    'r': '.-.', 
    's': '...', 
    't': '-',
    'u': '..--', 
    'v': '...-', 
    'w': '.--', 
    'x': '-..-',
    'y': '-.--', 
    'z': '--..', 
    '1': '.----',
    '2': '..---', 
    '3': '...--', 
    '4': '....-', 
    '5': '.....',
    '6': '-....', 
    '7': '--...', 
    '8': '---..', 
    '9': '----.',
    '0': '-----', 
    ' ':' ', 
    '|':'|', 
    "":"" }

morse_to_english = dict([(value, key) for key, value in english_to_morse.items()])

#define layout
#create frames

input_frame = tkinter.LabelFrame(root, bg=frame_color)
input_frame.pack(padx=16, pady=(16,8))
output_frame = tkinter.LabelFrame(root, bg=frame_color)
output_frame.pack(padx=16, pady=(8,16))


root.mainloop()