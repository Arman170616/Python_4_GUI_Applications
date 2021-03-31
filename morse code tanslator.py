import tkinter
from tkinter import IntVar, END


#Define window
root = tkinter.Tk()
root.title('morse code tanslator')
root.geometry('500x380')
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
def convert():
    ''' call the appropriate conversion function based off radio button values '''
    #English to morse code
    if language.get() == 1:
        get_morse() # here, 1= value
    elif language.get()  == 2:
        get_english() # here, 2 = value

def get_morse():
    """ convert an english to morse code  """
    #string to hold morse code  
    morse_code = ""

    #get the input text and standardize it to lower case 
    text = input_text.get('1.0', END)
    text = text.lower()

    #remove any letters of symbols not in our dict keys
    for letter in text:
        if letter not in english_to_morse.keys():
            text = text.replace(letter, '')
            
    #break up into individual words base on space " " and put into a list
    word_list = text.split(" ")
    print(word_list)

    #turn each individual word in word_list into a list of letters.
    for word in word_list:
        letters = list(word)
        print(letters)
        #for each letter, get the morse code representation and append it to the string morse_code
        for letter in letters:
            morse_char = english_to_morse[letter]
            morse_code += morse_char

            #seperate individual letters with a space
            morse_code += " "
        #Seperate individual words with a |
        morse_code += " "
        print(morse_code)
    output_text.insert('1.0', morse_code)

def get_english():
    print('english')





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


#layout for the input frame

input_text = tkinter.Text(input_frame, height=8, width=30, bg=text_color)
input_text.grid(row=0, column=1, rowspan=3, padx=5, pady=5)

language = IntVar()
language.set(1)
morse_button = tkinter.Radiobutton(input_frame, text="English --> Morse Code", variable=language, value=1, font=button_font, bg=frame_color) 
english_button = tkinter.Radiobutton(input_frame, text="Morse Code --> English", variable=language, value=2, font=button_font, bg=frame_color) 
guide_button = tkinter.Button(input_frame, text='Guide', font=button_font, bg=button_color)



morse_button.grid(row=0, column=0, pady=(15,0))
english_button.grid(row=1, column=0)
guide_button.grid(row=2, column=0, sticky='WE', padx=10)


#layout for the output frame

output_text = tkinter.Text(output_frame, height=8, width=30, bg=text_color)
output_text.grid(row=0, column=1, rowspan=4, padx=5, pady=5)


convert_button = tkinter.Button(output_frame, text='Convert', font=button_font, bg=button_color, command=convert)
play_button = tkinter.Button(output_frame, text='Play Morse', font=button_font, bg=button_color)
clear_button = tkinter.Button(output_frame, text='Clear', font=button_font, bg=button_color)
quit_button = tkinter.Button(output_frame, text='Quit', font=button_font, bg=button_color, command=root.destroy)


convert_button.grid(row=0, column=0, padx=10, ipadx=50) #converts ipadx defines column width
play_button.grid(row=1, column=0, padx=10,sticky='WE')
clear_button.grid(row=2, column=0, padx=10,sticky='WE')
quit_button.grid(row=3, column=0, padx=10,sticky='WE')






root.mainloop()