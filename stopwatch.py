import tkinter as tk
import time
import tkinter.messagebox

window = tk.Tk()
window.title("Stopwatch")
window.geometry("600x800")

def starts():
    hn = int(h.get())
    mn = int(m.get())
    sn = int(s.get())

    ts = hn*3600 + mn*60 + sn
    while ts > 00:
        ts = ts - 1
        hn = ts//3600
        mn = ts%3600//60
        sn = ts%60
        h1.set(hn)
        m1.set(mn)
        s1.set(sn)
        window.update()
        time.sleep(1)

    if ts == 0:
        tkinter.messagebox.showinfo("END", "Your timer has finished")



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