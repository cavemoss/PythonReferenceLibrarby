# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> place
from tkinter import *


# instance 1
root = Tk()
root.geometry('420x420+100+100')
root.title('place')

Button(master=root, text='a Thing 1').place(x=60, y=30, width=100, height=30)


# instance 2
win1 = Toplevel()
win1.geometry('420x420+600+100')
win1.title('place relative')

Button(master=win1, text='a Thing 1').place(relx=0.1, rely=0.1, relwidth=0.5, relheight=0.5)


root.mainloop()
