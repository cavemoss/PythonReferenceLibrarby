# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> root window
from tkinter import *

root = Tk()

root.geometry('420x420+400+400')
root.config(background='blue')
root.title('GUI')
root.resizable(False, False)
icon = PhotoImage(file='../(path)/picture.png')
root.iconphoto(True, icon)

root.mainloop()
