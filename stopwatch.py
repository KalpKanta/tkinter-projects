import tkinter as tk
import time

window = tk.Tk()
window.title = ("Stopwatch")
window.geometry = ("600x800")

def starts():
    hn = int(h.get())
    mn = int(m.get())
    sn = int(s.get())

    ts = hn*3600 + mn*60 + sn
    while ts >= 00:
        ts = ts - 1
        print(ts)
#time.sleep(1)


h1 = tk.StringVar()
m1 = tk.StringVar()
s1 = tk.StringVar()

h1.set("00")
m1.set("00")
s1.set("00")

h = tk.Entry(window, textvariable=h1)
h.grid(row = 1, column = 1)

m = tk.Entry(window, textvariable=m1)
m.grid(row = 1, column = 2)

s = tk.Entry(window, textvariable=s1)
s.grid(row = 1, column = 3)

start = tk.Button(window, text = "Start stopwatch", command = starts)
start.grid(row = 2, column = 2)

window.mainloop()