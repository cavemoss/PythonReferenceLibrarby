# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GUI input
from tkinter import *


def submit():
    username = entry.get()
    print('you are', str(username.capitalize()))
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get()) - 1, END)


root = Tk()

entry = Entry(root,
              font=('Arial', 20),
              fg='#00ff00',
              bg='black',
              # show='*'
              )

# entry.insert(0, 'YOU ARE/ ')
entry.pack(side=LEFT)

submit_button = Button(root, text='submit', command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(root, text='delete', command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(root, text='backspace', command=backspace)
backspace_button.pack(side=RIGHT)

root.mainloop()
