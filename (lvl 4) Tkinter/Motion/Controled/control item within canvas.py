# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> control item within canvas
from tkinter import *
s = 10


def up(event):
    canvas.move(image, 0, -s)


def left(event):
    canvas.move(image, -s, 0)


def right(event):
    canvas.move(image, +s, 0)


def down(event):
    canvas.move(image, 0, +s)


root = Tk()
canvas = Canvas(root, width=500, height=500)

root.bind('<w>', up)
root.bind('<d>', right)
root.bind('<a>', left)
root.bind('<s>', down)
root.bind('<Up>', up)
root.bind('<Right>', right)
root.bind('<Left>', left)
root.bind('<Down>', down)

img = PhotoImage(file='(path)\\picture.png')
image = canvas.create_image(0, 0, image=img, anchor=NW)
canvas.pack()

root.mainloop()
