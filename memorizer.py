import tkinter as tk
import tkinter.filedialog

def open_file():
    file1 = tkinter.filedialog.askopenfile()
    if file1 is not None:
        data = file1.readlines()
        for line in data:
            Lb_area.insert(tk.END, line)

def delete_file():
    index = Lb_area.curselection()
    if index:
        Lb_area.delete(index)

def save_file():
    file1 = tkinter.filedialog.asksaveasfile()
    if file1 is not None:
        for item in Lb_area.get(0, tk.END):
            print(item, file = file1)


def add_item():
    name = entry_field.get()
    Lb_area.insert(tk.END, name)

root = tk.Tk()
root.geometry("400x400")
root.title("Memorizer")

open_button = tk.Button(root, text="OPEN", command=open_file)
open_button.grid(column=1, row=1)

delete_button = tk.Button(root, text="DELETE", command=delete_file)
delete_button.grid(column=2, row=1)

save_button = tk.Button(root, text="SAVE", command=save_file)
save_button.grid(column=3, row=1)

entry_field = tk.Entry(root)
entry_field.grid(column=1, row=2, columnspan=2)

add_button = tk.Button(root, text="ADD", command=add_item)
add_button.grid(column=3, row=2)

Lb_area = tk.Listbox(root, height=10, width=30)
Lb_area.grid(column=1, row=3, columnspan=3)

root.mainloop()