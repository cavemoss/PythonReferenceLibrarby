# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GUI frame
from tkinter import *

root = Tk()
root.geometry('420x420')

frame = Frame(root, bg='pink', bd=5, relief=SUNKEN)
frame.place(x=0, y=0)

Button(frame, text='W', font=('Consolas', 25), width=3).pack(side=TOP)
Button(frame, text='A', font=('Consolas', 25), width=3).pack(side=LEFT)
Button(frame, text='S', font=('Consolas', 25), width=3).pack(side=LEFT)
Button(frame, text='D', font=('Consolas', 25), width=3).pack(side=LEFT)

root.mainloop()
