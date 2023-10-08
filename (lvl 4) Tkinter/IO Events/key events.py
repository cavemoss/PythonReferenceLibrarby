# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> key events
from tkinter import *


def any_key(event):
    print('you pressed:' + event.keysym + '\n')
    label.config(text=event.keysym)


def win(event):
    if event.keysym == 'W':
        print('W\nYOU WIN!\n')
    else:
        print('w\nYOU WIN!\n')


def resp(event):
    if event.keysym == 'F':
        print('F\nYOU WIN!\n')
    else:
        print('f\nYOU WIN!\n')


root = Tk()

root.bind('<Key>', any_key)
root.bind('<w>', win)
root.bind('<W>', win)
root.bind('<f>', resp)
root.bind('<F>', resp)

label = Label(root, font=('Consolas', 80))
label.pack()

root.mainloop()
