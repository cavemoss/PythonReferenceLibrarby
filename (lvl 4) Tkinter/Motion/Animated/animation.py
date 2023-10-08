# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> animation
from tkinter import *
import time
RUNNING = True


root = Tk()
WIDTH = HEIGHT = 106 * 5

canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

bg = PhotoImage(file='(path)\\happy_abby.gif').zoom(5, 5)
canvas.create_image(0, 0, image=bg, anchor=NW)

img = PhotoImage(file='(path)\\picture.png').subsample(2, 2)
image = canvas.create_image(0, 0, image=img, anchor=NW)

while RUNNING:
    coordinates = canvas.coords(image)
    print(coordinates)

    image_width = img.width()
    image_height = img.height()

    xVelocity = 3
    yVelocity = 2

    if coordinates[0] >= WIDTH - image_width or coordinates[0] < 0:
        xVelocity = -xVelocity
    if coordinates[1] >= HEIGHT - image_height or coordinates[1] < 0:
        yVelocity = -yVelocity

    canvas.move(image, xVelocity, yVelocity)

    root.update()
    time.sleep(0.01)

root.mainloop()
