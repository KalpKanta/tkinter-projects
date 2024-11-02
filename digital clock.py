#import tkinter as tk
#import time

#def update():
    #current_time = time.strftime("%Y:%m:%d:%H:%M:%S")
    #label.config(text = current_time)
    #label.after(1000, update)

#screen = tk.Tk()
#screen.geometry("800x600")
#screen.title("Digital clock")
#label = tk.Label(screen, text = "")
#label.pack()
#update()
#screen.mainloop()


import tkinter as tk
import time
import random

def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    rcolor = random.choice(colors)
    window.config(bg = rcolor)
    window.after(1000, update_time)

colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink"]

window = tk.Tk()
window.title("Clock")
window.configure(bg="red")

time_label = tk.Label(window, text="", fg="black", bg="red")
time_label.pack()

update_time()
window.mainloop()