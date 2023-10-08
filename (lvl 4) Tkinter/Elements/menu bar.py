# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GUI menu bar
from tkinter import *


def openfile():
    print('file has been opened')


def savefile():
    print('file has been saved')


def cut():
    print('cut')


def copy():
    print('copy')


def paste():
    print('paste')


root = Tk()

root_menubar = Menu(root)
root.config(menu=root_menubar)

FILE_menu = Menu(root_menubar, font=('Consolas', 12), tearoff=0)
root_menubar.add_cascade(label='File', menu=FILE_menu)

FILE_menu.add_command(label='open', command=openfile)
FILE_menu.add_command(label='save', command=savefile)
FILE_menu.add_separator()
FILE_menu.add_command(label='exit', command=quit)

EDIT_menu = Menu(root_menubar, tearoff=0, font=('Consolas', 12))
root_menubar.add_cascade(label='Edit', menu=EDIT_menu)

EDIT_menu.add_command(label='cut', command=cut)
EDIT_menu.add_command(label='copy', command=copy)
EDIT_menu.add_command(label='paste', command=paste)

root.mainloop()
