import tkinter as tk

window = tk.Tk()

window.title("python")

window.geometry("300x200")

nw = tk.Label(window,text="NW (North west)")
nw.grid(row=0,column=0)

n = tk.Label(window, text= "N(North)")
n.grid(row=0,column=2) 

ne = tk.Label(window,text= "NE(North East)")
ne.grid(row=0,column=4)

w = tk.Label(window,text= "W(West)")
w.grid(row=2,column=0)

e = tk.Label(window,text="E(East)")
e.grid(row=2,column=4)

sw = tk.Label(window,text="SW(Sourth West)")
sw.grid(row=4,column=0)

s = tk.Label(window,text="S(South)")
s.grid(row=4,column=2)

se = tk.Label(window,text="SE(Sourth East)")
se.grid(row=4,column=4)

window.mainloop()

