import tkinter as tk

window = tk.Tk()

window.title("Studyfied.com")

window.geometry("350x200")

frame = tk.LabelFrame(window, text="Check Group", padx=50, pady=10)
frame.pack(padx=70, pady=10, fill="both")

# tkinter variable types
# 1. BooleanVar()
# 2. StringVar()
# 3. IntVar()
# 4. DoubleVar()

check_var1 = tk.IntVar()

check1 = tk.Checkbutton(frame, text="Check One", variable=check_var1)
check1.pack(fill="both", anchor="w")


check_var2 = tk.IntVar()

check2 = tk.Checkbutton(frame, text="Check Two", variable=check_var2)
check2.pack(fill="both", anchor="w")

window.mainloop()


# x = 5
# print(x)

# y = tk.IntVar()
# y.set(5)
# print(y.get())
