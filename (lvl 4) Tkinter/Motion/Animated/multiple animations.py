# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> multiple animations
from tkinter import *
import time
RUNNING = True


class Ball:
    def __init__(self, canvas, x, y, diameter, x_velocity, y_velocity, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, diameter, diameter, fill=color)
        self.xVelocity = x_velocity
        self.yVelocity = y_velocity

    def move_bitch(self):
        coordinates = self.canvas.coords(self.image)

        if coordinates[2] >= self.canvas.winfo_width() or coordinates[0] < 0:
            self.xVelocity = -self.xVelocity
        if coordinates[3] >= self.canvas.winfo_height() or coordinates[1] < 0:
            self.yVelocity = -self.yVelocity

        self.canvas.move(self.image, self.xVelocity, self.yVelocity)


root = Tk()
WIDTH = HEIGHT = 500

thecanvas = Canvas(root, width=WIDTH, height=HEIGHT)
thecanvas.pack()

volley_ball = Ball(thecanvas, 0, 0, 100, 1, 1, 'white')
tennis_ball = Ball(thecanvas, 0, 0, 50, 4, 5, 'yellow')
basket_ball = Ball(thecanvas, 0, 0, 125, 8, 7, 'orange')

while RUNNING:
    volley_ball.move_bitch()
    tennis_ball.move_bitch()
    basket_ball.move_bitch()

    root.update()
    time.sleep(0.01)

root.mainloop()
