# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GUI checkbox
from tkinter import *


def display():
    if x.get() == 1:
        print('you agree')
    else:
        print('you disagree')


root = Tk()
root.geometry('600x420')
root.config(background='Black')
root.title('GUI')

photo = PhotoImage(file='(path)\\sadge_abby.gif')
x = IntVar()

check_button = Checkbutton(root,
                           text='you agree?',
                           font=('Arial', 30),

                           fg='white',
                           bg='blue',
                           activebackground='blue',
                           activeforeground='white',

                           padx=25,
                           pady=10,

                           image=photo,
                           compound='left',

                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display)
check_button.pack()

root.mainloop()
