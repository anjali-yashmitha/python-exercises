import tkinter as tk # PEP8: `import *` is not preferred
from tkinter.font import Font

def create_number_row():
 window = tk.Tk()
 window.title = ("Number Row")
 colors = ["red","blue", "green", "yellow", "orange"]
 for i in range(1,6):
     # cell = tk.Label(window, text = str(i), bg = colors[i-1], width = 5, height = 2)
     cell = tk.Label(window, text = str(i),font = Font(weight = "bold"), bg = colors[i-1],
     width = 5, height = 2)
     cell.grid(row = 0, column = i -1, padx = 5, pady = 5)
 window.mainloop()
create_number_row()