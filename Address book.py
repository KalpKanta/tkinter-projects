import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox

window = tk.Tk()
window.title("My Address Book")
window.geometry("600x600")

ab = {}

def save():
    savef = tkinter.filedialog.asksaveasfile()
    if savef is not None:
        print(ab, file = savef)
        contact_listbox.delete(0, tk.END)

def open():
    global ab
    savef =tkinter.filedialog.askopenfile()
    if savef is not None:
        ab = eval(savef.read())
        updatelb()

        
def updatelb():
    k = ab.keys()
    contact_listbox.delete(0,tk.END)
    for key in k:
        contact_listbox.insert(tk.END, key)

def add():
    
    n = name_entry.get()
    a = address_entry.get()
    m = mobile_entry.get()
    e = email_entry.get()
    b = birthday_entry.get()

    ab[n] = [a, m, e, b]
    updatelb()

def delete():
    d = contact_listbox.curselection()
    name = contact_listbox.get(d)
    del ab[name]
    updatelb()

def show_info(event):
    sd = contact_listbox.get(tk.ACTIVE)
    record = ab.get(sd)
    tkinter.messagebox.showinfo(sd, "Name: " + sd + "\nAddress: " + record[0] + "\nMobile: " + record[1] + "\nEmail: " + record[2] + "\nBirthday: " + record[3])

def edit():
    sd = contact_listbox.get(tk.ACTIVE)
    record = ab.get(sd)
    name_entry.insert(0, sd)
    address_entry.insert(0, record[0])
    mobile_entry.insert(0, record[1])
    email_entry.insert(0, record[2])
    birthday_entry.insert(0, record[3])

name_label = tk.Label(window, text="Name:")
name_entry = tk.Entry(window)

address_label = tk.Label(window, text="Address:")
address_entry = tk.Entry(window)

mobile_label = tk.Label(window, text="Mobile:")
mobile_entry = tk.Entry(window)

email_label = tk.Label(window, text="Email:")
email_entry = tk.Entry(window)

birthday_label = tk.Label(window, text="Birthday:")
birthday_entry = tk.Entry(window)

open_button = tk.Button(window, text="Open", command = open)
edit_button = tk.Button(window, text="Edit", command = edit)
delete_button = tk.Button(window, text="Delete", command = delete)
update_add_button = tk.Button(window, text="Update/Add", command = add)
save_button = tk.Button(window, text="Save", command = save)

contact_listbox = tk.Listbox(window, width=50, height=30)

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
address_label.grid(row=1, column=0)
address_entry.grid(row=1, column=1)
mobile_label.grid(row=2, column=0)
mobile_entry.grid(row=2, column=1)
email_label.grid(row=3, column=0)
email_entry.grid(row=3, column=1)
birthday_label.grid(row=4, column=0)
birthday_entry.grid(row=4, column=1)

open_button.grid(row=5, column=0)
edit_button.grid(row=5, column=1)
delete_button.grid(row=5, column=2)
update_add_button.grid(row=5, column=3)
save_button.grid(row=6, column=1, columnspan=3)

contact_listbox.grid(row=0, column=3, rowspan=5, padx=10, pady=10)
contact_listbox.bind('<<ListboxSelect>>', show_info)

window.mainloop()