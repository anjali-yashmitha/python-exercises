import tkinter as tk
# Create the main window
window = tk.Tk()
# Set the window title
window.title("Python")
lab1 = tk.Label(window, text = "Py GUI", bg = "blue", fg = "yellow")
lab1.pack()
# lab1.grid(row = 0, column = 0)
# lab1.place(x = 20, y = 30)
# Run the main event loop
window.mainloop()