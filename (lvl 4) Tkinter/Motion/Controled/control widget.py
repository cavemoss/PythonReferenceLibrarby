# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> control widget
from tkinter import *
s = 10


def up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() - s)


def left(event):
    label.place(x=label.winfo_x() - s, y=label.winfo_y())


def right(event):
    label.place(x=label.winfo_x() + s, y=label.winfo_y())


def down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() + s)


root = Tk()
root.geometry('500x500')

root.bind('<w>', up)
root.bind('<d>', right)
root.bind('<a>', left)
root.bind('<s>', down)
root.bind('<Up>', up)
root.bind('<Right>', right)
root.bind('<Left>', left)
root.bind('<Down>', down)

photo = PhotoImage(file='(path)\\picture.png')
label = Label(root, image=photo, bg='#dddddd')
label.place(x=0, y=10)

root.mainloop()
