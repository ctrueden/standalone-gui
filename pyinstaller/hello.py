import tkinter as tk
from tkinter import messagebox

def show_dialog():
    messagebox.showinfo("Dialog Box", "Hello, world!")

window = tk.Tk()

button = tk.Button(window, text="Show Dialog", command=show_dialog)
button.pack()

window.mainloop()
