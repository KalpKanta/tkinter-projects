import tkinter as tk
import time

def update():
    current_time = time.strftime("%Y:%m:%d:%H:%M:%S")
    label.config(text = current_time)
    label.after(1000, update)

screen = tk.Tk()
screen.geometry("800x600")
screen.title("Digital clock")
label = tk.Label(screen, text = "")
label.pack()
update()
screen.mainloop()