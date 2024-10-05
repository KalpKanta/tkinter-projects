import tkinter

screen = tkinter.Tk()
screen.geometry("800x600")
screen.configure(background = "white")
screen.title("tk")

def show_conversions():
   Kg = int(weight_entry.get())
   pounds = (Kg * 2.20462)
   grams = (Kg * 1000)
   ounces = (Kg * 35.274)
   text2.insert("1.0", pounds)
   text1.insert("1.0", grams)
   text3.insert("1.0", ounces)
weight_label = tkinter.Label(screen, text = "Enter the weight in Kg", font = ("times new roman", 10))
weight_label.grid(row = 1, column = 1)

weight_entry = tkinter.Entry(screen)
weight_entry.grid(row = 1, column = 2)

convert_button = tkinter.Button(screen, text = "Convert", command = show_conversions)
convert_button.grid(row = 1, column = 3)

grams_label = tkinter.Label(screen, text = "Grams")
grams_label.grid(row = 2, column = 1)

pounds_label = tkinter.Label(screen, text = "Pounds")
pounds_label.grid(row = 2, column = 2)

ounces_label = tkinter.Label(screen, text = "Ounces")
ounces_label.grid(row = 2, column = 3)

text1 = tkinter.Text(screen, width = 10, height = 1)
text1.grid(row = 3, column = 1)

text2 = tkinter.Text(screen, width = 10, height = 1)
text2.grid(row = 3, column = 2)

text3 = tkinter.Text(screen, width = 10, height = 1)
text3.grid(row = 3, column = 3)

screen.mainloop()