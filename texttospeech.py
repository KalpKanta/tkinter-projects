import tkinter as tk
import os
from gtts import gTTS

window = tk.Tk()
window.geometry("800x600")
window.title("Text To Speech")


def s():
    words = entry.get()
    myobj = gTTS(text = words, lang = "en", slow = False)
    myobj.save("sp.wav")
    
title = tk.Label(window, text = "Text to Speech Converter")
title.pack()
entry = tk.Entry(window)
entry.pack()
speech = tk.Button(window, text = "Make into speech", command = s)
speech.pack()

    
window.mainloop()