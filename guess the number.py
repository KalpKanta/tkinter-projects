import tkinter as tk
import random

window = tk.Tk()
window.title("guess the number game")
window.geometry("800x600")


welcome_label = tk.Label(window, text = "Welcome to our game", padx = 70, pady = 30)
welcome_label.grid(row = 1, column = 1, columnspan = 2)

name_label = tk.Label(window, text = "whats your name?", padx = 70, pady = 30)
name_label.grid(row = 2, column = 1)

guess_label = tk.Label(window, text = "take a guess:", padx = 70, pady = 30)
guess_label.grid(row = 4, column = 1)

name_entry = tk.Entry(window)
name_entry.grid(row = 3, column = 1)

guess_entry = tk.Entry(window)
guess_entry.grid(row = 5, column = 1)

ok_button = tk.Button(window, text = "Ok", padx = 70, pady = 20)
ok_button.grid(row = 3, column = 2)

guess_button = tk.Button(window, text = "Guess", padx = 70, pady = 20)
guess_button.grid(row = 4, column = 2)
window.mainloop()