import tkinter as tk
# Create the main window
window = tk.Tk()
# Set the window title
window.title("Python")
# Set the window size
window.geometry("300x200")

# Create a label widget
lab = tk.Label(window, text="ආයුබ ෝ,වන්, வணக்கம், عليكم السالم")
# Pack the label widget onto the window
lab.pack()

# Run the main event loop
window.mainloop()