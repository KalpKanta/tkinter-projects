import tkinter as tk

def change_bg(event):
    selected_color = color_listbox.get(tk.ACTIVE)
    window.config(bg=selected_color)

def add_color():
    new_color = color_entry.get()
    color_listbox.insert(tk.END, new_color)
    color_entry.delete(0, tk.END)

def remove_color():
    selected_index = color_listbox.curselection()
    if selected_index:
        color_listbox.delete(selected_index)

# Create the main window
window = tk.Tk()
window.title("Color Changer")

# Create a listbox for color choices
color_listbox = tk.Listbox(window)
color_listbox.pack(pady=10)
color_listbox.insert(tk.END, "red", "blue", "green", "yellow", "orange", "purple")
color_listbox.bind('<<ListboxSelect>>', change_bg)

# Create an entry field to add new colors
color_entry = tk.Entry(window)
color_entry.pack(pady=5)

# Create buttons to add and remove colors
add_button = tk.Button(window, text="Add Color", command=add_color)
add_button.pack(pady=5)

remove_button = tk.Button(window, text="Remove Color", command=remove_color)
remove_button.pack(pady=5)

window.mainloop()