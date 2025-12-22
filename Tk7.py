import tkinter as tk
from tkinter import ttk

def button_click():
    hello_label.config(text="Button Clicked!")

def show_text():
    text = entry.get()
    output_label.config(text="You entered: " + text)

def show_checkbox_state():
    if checkbox_var.get():
        checkbox_label.config(text="Checkbox is checked")
    else:
        checkbox_label.config(text="Checkbox is unchecked")

def add():
    result_entry.delete(0, tk.END)
    n1 = int(num1_entry.get())
    n2 = int(num2_entry.get())
    result_entry.insert(tk.END, str(n1 + n2))

def subtract(event=None):
    result_entry.delete(0, tk.END)
    n1 = int(num1_entry.get())
    n2 = int(num2_entry.get())
    result_entry.insert(tk.END, str(n1 - n2))

window = tk.Tk()
window.title("Combined Tkinter App")
window.geometry("900x600")

hello_label = tk.Label(window, text="Hello, Tkinter!")
hello_label.place(x=20, y=20)

click_btn = tk.Button(window, text="Click Me", command=button_click)
click_btn.place(x=20, y=50)

entry = tk.Entry(window)
entry.place(x=20, y=100)

show_btn = tk.Button(window, text="Show Text", command=show_text)
show_btn.place(x=20, y=130)

output_label = tk.Label(window, text="")
output_label.place(x=20, y=160)

checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(window, text="Check me!", variable=checkbox_var, command=show_checkbox_state)
checkbox.place(x=20, y=210)

checkbox_label = tk.Label(window, text="Checkbox is unchecked")
checkbox_label.place(x=20, y=240)

data = ("one", "two", "three", "four")
combo = ttk.Combobox(window, values=data)
combo.place(x=300, y=20)
combo.set("one")

listbox = tk.Listbox(window, height=4, selectmode="multiple")
for item in data:
    listbox.insert(tk.END, item)
listbox.place(x=300, y=60)

gender = tk.IntVar(value=1)
rb1 = tk.Radiobutton(window, text="Male", variable=gender, value=1)
rb2 = tk.Radiobutton(window, text="Female", variable=gender, value=2)
rb1.place(x=300, y=140)
rb2.place(x=370, y=140)

v1 = tk.IntVar()
v2 = tk.IntVar()
c1 = tk.Checkbutton(window, text="Cricket", variable=v1)
c2 = tk.Checkbutton(window, text="Tennis", variable=v2)
c1.place(x=300, y=180)
c2.place(x=380, y=180)

tk.Label(window, text="First Number").place(x=550, y=20)
tk.Label(window, text="Second Number").place(x=550, y=60)
tk.Label(window, text="Result").place(x=550, y=140)

num1_entry = tk.Entry(window)
num2_entry = tk.Entry(window)
result_entry = tk.Entry(window)

num1_entry.place(x=680, y=20)
num2_entry.place(x=680, y=60)
result_entry.place(x=680, y=140)

add_btn = tk.Button(window, text="Add", command=add)
sub_btn = tk.Button(window, text="Subtract")
sub_btn.bind("<Button-1>", subtract)

add_btn.place(x=580, y=100)
sub_btn.place(x=680, y=100)

window.mainloop()
