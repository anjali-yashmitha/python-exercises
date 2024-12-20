import tkinter as tk            # PEP8: `import *` is not preferred
def main(root):
   global img # <-- solution for bug

   img = tk.PhotoImage(file="d:/xy/rose.png")
   label = tk.Label(image=img)
   label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    main(root)
    root.mainloop()
