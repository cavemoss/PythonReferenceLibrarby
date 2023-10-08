# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> grid geometry manager
from tkinter import *

root = Tk()

Label(root, text='submit your info', font=('Consolas', 20)).grid(row=0, column=0, columnspan=2)

Label(root, text='First name: ', bg='red', width=20).grid(row=1, column=0)
Entry(root).grid(row=1, column=1)

Label(root, text='Last name: ', bg='green').grid(row=2, column=0)
Entry(root).grid(row=2, column=1)

Label(root, text='Email: ', fg='white', bg='blue', width=30).grid(row=3, column=0)
Entry(root).grid(row=3, column=1)

Button(root, text='Submit').grid(row=4, column=0, columnspan=2)

root.mainloop()
