import tkinter as tk

root = tk.Tk()
root.title("Coloured Number Square")
root.geometry("200x200")

canvas = tk.Canvas(root, width=150, height=150)
canvas.pack()

canvas.create_rectangle(50, 50, 100, 100, fill="pink")  # Create a pink square
canvas.create_text(75, 75, text="1", fill="purple", font=("Arial", 24))  # Display the number '1'

root.mainloop()