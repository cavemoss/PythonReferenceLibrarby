# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> OS color chooser
from tkinter import *
from tkinter import colorchooser


def click():
    color = colorchooser.askcolor()
    print(color)

    color_hex = color[1]
    print(color_hex)

    root.config(background=color_hex)

    root.config(background=colorchooser.askcolor()[1])


root = Tk()
root.geometry('420x420')

Button(text='click this', command=click).pack()

root.mainloop()
