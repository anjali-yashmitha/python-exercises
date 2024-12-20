import tkinter as tk
# Create the main window
window = tk.Tk()
# Set the window title
window.title("Python")
im = tk.PhotoImage(file = 'D:/XY/SL_Flag.png')
small_image = im.subsample(2,2)
lab1 = tk.Label(window, image = small_image)
# large_image = small_image.zoom(2,2)
# lab1 = tk.Label(window, image = large_image)
lab1.pack()
# lab1.grid(row = 0, column = 0)
# lab1.place(x = 20, y = 30)
# Run the main event loop
window.mainloop()
