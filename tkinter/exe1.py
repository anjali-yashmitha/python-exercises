import tkinter as tk

window = tk.Tk()

window.title("Python Grid Example")

window.geometry("350x200")

label1 = tk.Label(window, text="Labal 1")
label1.grid(row=0, column=0)

label2 = tk.Label(window, text="Labal 2")
label2.grid(row=1, column=0)

label3 = tk.Label(window, text="Labal 3")
label3.grid(row=0, column=1)

label4 = tk.Label(window, text="Labal4")
label4.grid(row=1, column=1)

window.mainloop()
