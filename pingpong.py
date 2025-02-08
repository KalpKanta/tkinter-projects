import tkinter as tk
import random
import time

window = tk.Tk()
window.geometry("800x600")
window.title("ping pong")

canvas = tk.Canvas(window, width = 800, height = 600, bg = "black")
canvas.grid(row = 0, column = 0)
canvas.create_line(400, 0, 400, 600, fill = "White", width=2)
canvas.create_oval(300, 200, 500, 400, outline="White")
scoreboard = canvas.create_text(400, 20, text = "0:0", fill = "white", font = ("times new roman", 30,"bold"))

class Ball():
    def __init__(self):
        self.ball = canvas.create_oval(400, 300, 420, 320, fill="white")
        self.directions = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
        self.changex = random.choice(self.directions)
        self.changey = random.choice(self.directions)
        self.score1 = 0
        self.score2 = 0

    def draw(self):
        canvas.move(self.ball, self.changex, self.changey)
        self.cords = canvas.coords(self.ball)
        if self.cords[0] <= 0:
            self.changex = 4
            self.score2 = self.score2 + 1
        if self.cords[2] >= 800:
            self.changex = -4
            self.score1 = self.score1 + 1
        if self.cords[3] >= 600:
            self.changey = -4
        if self.cords[1] <= 0:
            self.changey = 4

class Player1():
    def __init__(self):
        self.p1 = canvas.create_rectangle(10, 250, 25, 350, fill = "white")
        self.changey = 0
        self.changex = 0
        canvas.bind_all("w", self.mpu)
        canvas.bind_all("s", self.mpd)
    def draw(self):
        canvas.move(self.p1,self.changex, self.changey)
        self.cords = canvas.coords(self.p1)
        if self.cords[1] <= 0:
            self.changey = 0
        if self.cords[3] >= 600:
            self.changey = 0
    
    def mpd(self, event):
        self.changey = 3

    def mpu(self, event):
        self.changey = -3


class Player2():
    def __init__(self):
        self.p2 = canvas.create_rectangle(775, 250, 790, 350, fill = "white")
        self.changey = 0
        self.changex = 0
        canvas.bind_all("<KeyPress-Up>", self.mpu)
        canvas.bind_all("<KeyPress-Down>", self.mpd)
    def draw(self):
        canvas.move(self.p2,self.changex, self.changey)
        self.cords = canvas.coords(self.p2)
        if self.cords[1] <= 0:
            self.changey = 0
        if self.cords[3] >= 600:
            self.changey = 0
    
    def mpd(self, event):
        self.changey = 3

    def mpu(self, event):
        self.changey = -3
        

p1 = Player1()
p2 = Player2()
ball1 = Ball()
while True:
    ball1.draw()
    p1.draw()
    p2.draw()
    window.update_idletasks()
    window.update()
    time.sleep(0.01)
window.mainloop()