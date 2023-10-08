# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> mouse events
from tkinter import *


def leftclick(event):
    print('you left-clicked ' + str(event.x) + ',' + str(event.y))


def rightclick(event):
    print('you right-clicked ' + str(event.x) + ',' + str(event.y))


def midclick(event):
    print('you mid-clicked ' + str(event.x) + ',' + str(event.y))


def release(event):
    print('release')


def entered(event):
    print('the mouse entered at ' + str(event.x) + ',' + str(event.y))


def left(event):
    print('the mouse left at ' + str(event.x) + ',' + str(event.y))


def motion(event):
    print('the mouse is at ' + str(event.x) + ',' + str(event.y))


root = Tk()

root.bind('<Button-1>', leftclick)
root.bind('<Button-3>', rightclick)
root.bind('<Button-2>', midclick)
root.bind('<ButtonRelease>', release)
root.bind('<Enter>', entered)
root.bind('<Leave>', left)
root.bind('<Motion>', motion)

root.mainloop()
