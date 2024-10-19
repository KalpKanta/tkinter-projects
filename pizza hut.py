import tkinter as tk

def place_order():
    pizza = pizza_var.get()
    quantity = int(quantity_entry.get())
    size = size_var.get()

    order_label.config(text=f"You ordered {quantity} {pizza} {size} sized pizza(s).")

root = tk.Tk()
root.title("Pizza Order")

pizza_var = tk.StringVar()
pizza_var.set("Veg Extravaganza")

quantity_entry = tk.Entry(root)

size_var = tk.StringVar()
size_var.set("S")

pizza_label = tk.Label(root, text="Pizza:")
pizza_label.grid(row=0, column=0)

pizza_dropdown = tk.OptionMenu(root, pizza_var, "Veg Extravaganza", "Pepperoni", "Margherita")
pizza_dropdown.grid(row=0, column=1)

quantity_label = tk.Label(root, text="Quantity:")
quantity_label.grid(row=1, column=0)

quantity_entry.grid(row=1, column=1)

size_label = tk.Label(root, text="Size:")
size_label.grid(row=2, column=0)

size_radio1 = tk.Radiobutton(root, text="S", variable=size_var, value="S")
size_radio1.grid(row=2, column=1)

size_radio2 = tk.Radiobutton(root, text="M", variable=size_var, value="M")
size_radio2.grid(row=2, column=2)

size_radio3 = tk.Radiobutton(root, text="L", variable=size_var, value="L")
size_radio3.grid(row=2, column=3)

order_button = tk.Button(root, text="Order", command=place_order)
order_button.grid(row=3, column=0, columnspan=4)

order_label = tk.Label(root, text="")
order_label.grid(row=4, column=0, columnspan=4)

root.mainloop()