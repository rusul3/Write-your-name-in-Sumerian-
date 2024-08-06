import tkinter as tk
from tkinter import Frame, messagebox, font
from turtle import width
from PIL import Image, ImageTk
import os
import sys

# Define the Sumerian translation function
def translate_to_sumerian(text):
    sumerian_mapping = {
    'a': '𒀭', 'b': '𒁀', 'c': '𒁁', 'd': '𒁂', 'e': '𒁃',
    'f': '𒁄', 'g': '𒁅', 'h': '𒁆', 'i': '𒁇', 'j': '𒁈',
    'k': '𒁉', 'l': '𒁊', 'm': '𒁋', 'n': '𒁌', 'o': '𒁍',
    'p': '𒁎', 'q': '𒁏', 'r': '𒁐', 's': '𒁑', 't': '𒁒',
    'u': '𒁓', 'v': '𒁔', 'w': '𒁕', 'x': '𒁖', 'y': '𒁗', 'z': '𒁘'
}
    #translated_text = ''.join(sumerian_mapping.get(letter, '  ') for letter in text.lower())
    words = text.lower().split()  # Split input text into words
    translated_words = ["".join(sumerian_mapping.get(letter, ' ') for letter in word) for word in words]
    return '\n'.join(translated_words)  # Join words with newline for display
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Define the GUI layout
def create_gui():
    root = tk.Tk()
    root.title(" Write your name in Sumerian ")

    # Set the window size and make it not resizable
    root.geometry('800x750')  # Width x Height
    root.resizable(False, False)
    imageBACK = Image.open(resource_path("images/background2.jpg"))
    imageBACK = imageBACK.resize((800, 750))
    photo1 = ImageTk.PhotoImage(imageBACK)
    backgroundAAP = tk.Label(root, image=photo1)
    backgroundAAP.image = photo1
    backgroundAAP.place(x=0, y=0)
    # Define a suitable font
    input_font = font.Font(size=16)
    label_font = font.Font(size=14)
    
    cuneiform_font = font.Font(family='Noto Sans Cuneiform', size=30)  
   # define background 
    colorB = "#F0D3C5" 
    # Create widgets
    tk.Label(root, text="Enter your name please :" , font=label_font, background=colorB).place( x=160, y= 55)
    input_text = tk.Entry(root, font=input_font )
    input_text.place(x=380, y=55)
    
    result_label = tk.Label(root, text="Your name in Sumerian ", fg="#473021", font=cuneiform_font, background="#E2C6B8")
    result_label.place(x=170, y=330)

    # Function to update the label with the translation
    def translate_and_display():
        english_text = input_text.get()
        sumerian_text = translate_to_sumerian(english_text)
        result_label.config(text=sumerian_text)

    # Button to trigger translation
    imageButton = Image.open(resource_path("images/pen.jpg") )
    imageButton = imageButton.resize((120, 50))
    photo2 = ImageTk.PhotoImage(imageButton)  
    translate_button = tk.Button(root, image=photo2, background="#E2C6B8", command=translate_and_display)
    translate_button.place(x=350, y=120)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()

