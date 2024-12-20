import tkinter as tk
# Create the main window
window = tk.Tk()
# Set the window title
window.title("Python")

im = tk.PhotoImage(file = 'D:/XY/SL_flag.png')
small_image = im.subsample(2,2)
large_image = small_image.zoom(2,2)
# lab1 = tk.Label(window, image = large_image)
lab1.pack()

# Run the main event loop
window.mainloop()