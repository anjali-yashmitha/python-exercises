import tkinter as tk
def button():
 print("Button Clicked")

root = tk.Tk()
but = tk.Button(root, text="CLICK", fg="Yellow", bg="blue", command=button)
but.pack()
root.mainloop()