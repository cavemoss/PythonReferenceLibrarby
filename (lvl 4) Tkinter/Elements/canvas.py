# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GUI canvas
from tkinter import *

root = Tk()

canvas = Canvas(root, height=500, width=500, bg='white')
canvas.pack()

canvas.create_line(0, 0, 500, 500, fill='blue', width=5)
canvas.create_line(0, 500, 500, 0, fill='white', width=20)
canvas.create_line(0, 500, 500, 0, fill='red', width=5)

p = [250, 0, 500, 500, 0, 500]
canvas.create_rectangle(50, 50, 250, 250, fill='purple')
canvas.create_polygon(p, fill='yellow', outline='black', width=5)

canvas.create_arc(0, 0, 500, 500, style=CHORD, fill='green')
canvas.create_arc(0, 0, 250, 1000, style=ARC, outline='green', width=6)
canvas.create_arc(0, 0, 500, 500, style=PIESLICE, start=180, extent=180)

canvas.create_arc(0, 0, 500, 500, fill='red', extent=180, width=10)
canvas.create_arc(0, 0, 500, 500, fill='white', start=180, extent=180, width=10)
canvas.create_oval(190, 190, 310, 310, fill='white', width=10)

root.mainloop()
