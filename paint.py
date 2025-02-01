import tkinter as tk
from tkinter.colorchooser import askcolor

class Paint():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Paint")
        self.root.geometry("800x600")

        self.pen = tk.Button(self.root, text = "pen", command = self.pen1)
        self.pen.grid(row = 1, column = 0)
        self.brush = tk.Button(self.root, text = "brush", command = self.brush1)
        self.brush.grid(row = 1, column = 1)
        self.color = tk.Button(self.root, text = "color", command = self.color1)
        self.color.grid(row = 1, column = 2)
        self.eraser = tk.Button(self.root, text = "eraser", command = self.eraser1)
        self.eraser.grid(row = 1, column = 3)
        self.brushs = tk.Scale(self.root, from_ = 1, to = 10, orient = "horizontal")
        self.brushs.grid(row = 1, column = 4)
        self.canvas = tk.Canvas(self.root, width = 800, height = 550, background = "light grey")
        self.canvas.grid(row = 2, column = 0, columnspan = 5)
        self.setup()
        self.root.mainloop()

    def pen1(self):
        self.activate_button(self.pen)
        self.eraseron = False

    def brush1(self):
        self.activate_button(self.brush)
        self.eraseron = False

    def color1(self):
        self.pcolor = askcolor()[1]

    def eraser1(self):
        self.activate_button(self.eraser)
        self.eraseron = True

    def activate_button(self, sbutton):
        self.activeb.config(relief = tk.RAISED)
        self.activeb = sbutton
        self.activeb.config(relief = tk.SUNKEN)


    def draw(self, event):
        if self.eraseron == True:
            self.pencolor = "light grey"
        else:
            self.pencolor = self.pcolor

        self.psize = self.brushs.get()
        if self.xmpos and self.ympos:
            self.canvas.create_line(self.xmpos, self.ympos, event.x, event.y, width = self.psize, fill = self.pencolor, smooth = True, capstyle = tk.ROUND, splinesteps = 36)
        self.xmpos = event.x
        self.ympos = event.y

    def reset(self, event):
        self.xmpos = None
        self.ympos = None

    def setup(self):
        self.xmpos = None
        self.ympos = None
        self.pcolor = "black"
        self.psize = 1
        self.activeb = self.pen
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.reset)
        self.eraseron = False

Paint()