from tkinterimport*

root = Tk()
canvas = Canvas()
# create_oval() method - Creating a circle
canvas.create_oval(10, 10, 80, 80, outline = "black", fill = "purple",width = 2)
canvas.create_oval(110,10,210,110,outline = "black",fill = "white",width = 2)
canvas.pack()
root.mainloop()