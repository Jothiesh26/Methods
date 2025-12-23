import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Multi Page App")
        self.geometry("500x350")

        self.frames = []
        for F in (Page1, Page2, Page3, Page4, Page5):
            frame = F(self)
            self.frames.append(frame)
            frame.place(relwidth=1, relheight=1)

        self.show_frame(0)

    def show_frame(self, index):
        self.frames[index].tkraise()


class Page1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        label = tk.Label(self, text="Hello, Tkinter!", font=("Arial", 16))
        label.pack(pady=20)

        def button_click():
            label.config(text="Button Clicked!")

        tk.Button(self, text="Click Me", command=button_click).pack()
        tk.Button(self, text="Next ▶", command=lambda: parent.show_frame(1)).pack(side="right", padx=10, pady=10)


class Page2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        entry = tk.Entry(self)
        entry.pack(pady=10)

        output = tk.Label(self, text="")
        output.pack(pady=10)

        def show_text():
            output.config(text="You entered: " + entry.get())

        tk.Button(self, text="Show Text", command=show_text).pack()

        tk.Button(self, text="◀ Back", command=lambda: parent.show_frame(0)).pack(side="left", padx=10, pady=10)
        tk.Button(self, text="Next ▶", command=lambda: parent.show_frame(2)).pack(side="right", padx=10, pady=10)


class Page3(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        var = tk.BooleanVar()
        label = tk.Label(self, text="Checkbox is unchecked")
        label.pack(pady=10)

        def show_state():
            if var.get():
                label.config(text="Checkbox is checked")
            else:
                label.config(text="Checkbox is unchecked")

        tk.Checkbutton(self, text="Check me!", variable=var, command=show_state).pack()

        tk.Button(self, text="◀ Back", command=lambda: parent.show_frame(1)).pack(side="left", padx=10, pady=10)
        tk.Button(self, text="Next ▶", command=lambda: parent.show_frame(3)).pack(side="right", padx=10, pady=10)


class Page4(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        data = ("one", "two", "three", "four")

        ttk.Combobox(self, values=data).pack(pady=5)

        lb = tk.Listbox(self, selectmode="multiple")
        for i in data:
            lb.insert(tk.END, i)
        lb.pack(pady=5)

        v = tk.IntVar(value=1)
        tk.Radiobutton(self, text="Male", variable=v, value=1).pack()
        tk.Radiobutton(self, text="Female", variable=v, value=2).pack()

        tk.Checkbutton(self, text="Cricket").pack()
        tk.Checkbutton(self, text="Tennis").pack()

        tk.Button(self, text="◀ Back", command=lambda: parent.show_frame(2)).pack(side="left", padx=10, pady=10)
        tk.Button(self, text="Next ▶", command=lambda: parent.show_frame(4)).pack(side="right", padx=10, pady=10)


class Page5(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        tk.Label(self, text="First Number").pack()
        t1 = tk.Entry(self)
        t1.pack()

        tk.Label(self, text="Second Number").pack()
        t2 = tk.Entry(self)
        t2.pack()

        tk.Label(self, text="Result").pack()
        t3 = tk.Entry(self)
        t3.pack()

        def add():
            t3.delete(0, tk.END)
            t3.insert(tk.END, int(t1.get()) + int(t2.get()))

        def sub():
            t3.delete(0, tk.END)
            t3.insert(tk.END, int(t1.get()) - int(t2.get()))

        tk.Button(self, text="Add", command=add).pack(pady=5)
        tk.Button(self, text="Subtract", command=sub).pack(pady=5)

        tk.Button(self, text="◀ Back", command=lambda: parent.show_frame(3)).pack(pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
