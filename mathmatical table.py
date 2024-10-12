import tkinter as tk
import tkinter.ttk

number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
screen = tk.Tk()
screen.geometry("800x600")
screen.configure(background = "white")
screen.title("mathmatical table")

label1 = tk.Label(screen, text = "Mathmatical table")
label1.place(x = 325, y = 0)

label2 = tk.Label(screen, text = "Number and Range :")
label2.place(x = 60, y=100)

numbers = tkinter.ttk.Combobox(screen)
numbers["values"] = number
numbers.place(x = 310, y = 100)

button = tk.Button(screen, text = "Generate")
button.place(x = 345, y = 200)

choice = tk.IntVar()
choice.set(0)

button10 = tk.Radiobutton(screen, text = "10", variable = choice, value = 10)
button10.place(x = 600, y = 100)

button20 = tk.Radiobutton(screen, text = "20", variable = choice, value = 20)
button20.place(x = 600, y = 150)

button30 = tk.Radiobutton(screen, text = "30", variable = choice, value = 30)
button30.place(x = 600, y = 200)
screen.mainloop()