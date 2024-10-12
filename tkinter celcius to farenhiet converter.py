import tkinter as tk

def convert_to_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_label.config(text=f"Temperature in Fahrenheit: {fahrenheit:.1f}")
    except ValueError:
        fahrenheit_label.config(text="Please enter a valid number.")

window = tk.Tk()
window.title("Celsius to Fahrenheit Converter")

celsius_label = tk.Label(window, text="Enter Temperature in Celsius:")
celsius_label.grid(row=0, column=0)

celsius_entry = tk.Entry(window)
celsius_entry.grid(row=0, column=1)

fahrenheit_label = tk.Label(window, text="Temperature in Fahrenheit:")
fahrenheit_label.grid(row=1, column=0, columnspan=2)

convert_button = tk.Button(window, text="Convert", command=convert_to_fahrenheit)
convert_button.grid(row=2, column=0, columnspan=2)

window.mainloop()