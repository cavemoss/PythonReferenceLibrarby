# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> additional windows
from tkinter import *


def create_win():
    win1 = Toplevel()
    win1.title('dependant')

    win2 = Tk()
    win2.title('independent')


def create_del():
    root.destroy()
    root2 = Tk()
    root2.title('new window')

root = Tk()

Button(root, text='Create', command=create_win).pack()
Button(root, text='Create and Delete', command=create_del).pack()

root.mainloop()
