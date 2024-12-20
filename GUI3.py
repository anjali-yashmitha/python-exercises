import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("House")

# Create the Canvas widget
canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

# Draw the house structure
canvas.create_rectangle(80, 80, 220, 180, outline="black", fill="pink") # Main structure

# Draw the roof
canvas.create_polygon(50, 80, 150, 30, 250, 80, outline="black", fill="black") # Triangular roof

# Draw the door
canvas.create_rectangle(130, 140, 170, 180, outline="black", fill="brown") # Door

# Draw a window
canvas.create_rectangle(90, 100, 120, 130, outline="black", fill="brown") # Window

# Start the main event loop
root.mainloop()
