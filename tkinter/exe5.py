import tkinter as tk

window = tk.Tk()

window.title("tk")

window.geometry("300x200")

name_label = tk.Label(window, text="Name")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=10)

name_label = tk.Label(window, text="Email")
name_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

name_entry = tk.Entry(window)
name_entry.grid(row=1, column=1, padx=10, pady=10)

name_label = tk.Label(window, text="password")
name_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

name_entry = tk.Entry(window)
name_entry.grid(row=2, column=1, padx=10, pady=10)

window.mainloop()