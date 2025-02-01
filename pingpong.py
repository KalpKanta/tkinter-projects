import tkinter as tk
import random

window = tk.Tk()
window.geometry("800x600")
window.title("ping pong")

canvas = tk.Canvas(window, width = 800, height = 600, bg = "black")
canvas.grid(row = 0, column = 0)
canvas.create_line(400, 0, 400, 600, fill = "White", width=2)
canvas.create_oval(300, 200, 500, 400, outline="White")

class Ball():
    def __init__(self):
        self.ball = canvas.create_oval(400, 300, 420, 320, fill="white")
        self.directions = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        self.changex = random.choice(self.directions)
        self.changey = random.choice(self.directions)
        self.score1 = 0
        self.score2 = 0

    def draw(self):
        canvas.move(self.ball, self.changex, self.changey)
        self.cords = canvas.coords(self.ball)


ball1 = Ball()
while True:
    ball1.draw()
    window.update_idletasks()
    window.update()
window.mainloop()