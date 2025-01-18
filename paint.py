import tkinter as tk

class Paint():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Paint")
        self.root.geometry("800x600")

        self.pen = tk.Button(self.root, text = "pen")
        self.pen.grid(row = 1, column = 0)
        self.brush = tk.Button(self.root, text = "brush")
        self.brush.grid(row = 1, column = 1)
        self.color = tk.Button(self.root, text = "color")
        self.color.grid(row = 1, column = 2)
        self.eraser = tk.Button(self.root, text = "eraser")
        self.eraser.grid(row = 1, column = 3)
        self.brushs = tk.Scale(self.root, from_ = 1, to = 10, orient = "horizontal")
        self.brushs.grid(row = 1, column = 4)
        self.canvas = tk.Canvas(self.root, width = 800, height = 550, background = "light grey")
        self.canvas.grid(row = 2, column = 0, columnspan = 5)

        self.root.mainloop()

Paint()