import tkinter as tk

def button_click():
    label.config(text="Button Clicked!")

window = tk.Tk()
window.title("Simple Tkinter App")

label = tk.Label(window, text="Hello, Tkinter!")
label.pack(pady=20)

button = tk.Button(window, text="Click Me", command=button_click)
button.pack()

window.mainloop()
