import tkinter
import calendar

screen = tkinter.Tk()
screen.geometry("800x600")
screen.configure(background = "white")
screen.title("tkinter calendar hw")

def show_calendar():
   year = int(entry.get())
   screen2 = tkinter.Tk()
   screen2.geometry("800x600")
   screen2.configure(background = "white")
   screen2.title("tkinter calendar hw")
   text = tkinter.Text(screen2, height = 100)
   calendar_text =  calendar.calendar(year)
   text.insert("1.0", calendar_text)
   text.pack()
   screen2 .mainloop()
def exit():
   screen.destroy()


label1 = tkinter.Label(screen, text = "Calendar",  bg = "grey", font = ("times new roman", 50, "italic"))
label1.pack()

label2 = tkinter.Label(screen, text = "Enter Year", bg = "lime")
label2.pack()

entry = tkinter.Entry(screen)
entry.pack()

button1 = tkinter.Button(screen, text = "Show Calendar", background = "red", command = show_calendar)
button1.pack()

button2 = tkinter.Button(screen, text = "Exit", background = "red", command = exit)
button2.pack()

screen.mainloop()