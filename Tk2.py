import tkinter as tk

def show_text():
    text = entry.get()
    output_label.config(text="You entered: " + text)

window = tk.Tk()
window.title("Entry and Output App")

entry = tk.Entry(window)
entry.pack(pady=10)

show_button = tk.Button(window, text="Show Text", command=show_text)
show_button.pack()

output_label = tk.Label(window, text="")
output_label.pack(pady=10)

window.mainloop()