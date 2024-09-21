import tkinter

screen = tkinter.Tk()
screen.geometry("800x600")
screen.configure(background = "black")
screen.title("tkinter basics")

label = tkinter.Label(screen, text = "hi im kalp")
label.pack()

entry = tkinter.Entry(screen)
entry.pack()

text = tkinter.Text(screen)
text.pack()

button = tkinter.Button(screen, text = "open")
button.pack()
screen.mainloop() 