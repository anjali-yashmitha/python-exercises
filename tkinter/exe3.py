import tkinter as tk

window = tk.Tk()

window.title("tk")

window.geometry("300x200")


frame = tk.LabelFrame(window, text="This is Label Frame", padx=10, pady=10)
frame.pack(padx=10, pady=10, fill="both", expand=True)

lab1 = tk.Label(frame, text="1. This is a Label.")
lab1.pack(anchor="w")

lab2 = tk.Label(frame, text="2.This is another Label.")
lab2.pack(anchor="w")

lab3 = tk.Label(frame, text="3. We can add multiple widgets in it.")
lab3.pack(anchor="w")


window.mainloop()
