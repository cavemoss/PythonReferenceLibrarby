# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GUI scale
from tkinter import *


def submit():
    print(str(scale.get()) + 'hp')


root = Tk()
root.geometry('420x420')

scale = Scale(root,
              from_=0, to=1000,
              resolution=100,

              length=600,
              orient=HORIZONTAL,

              troughcolor='#69EAFF',
              fg='#ff1c00',
              bg='#111111',

              tickinterval=200,
              font=('Consolas', 10),
              showvalue=False)
# scale.set((scale['to'] - scale['from'])/2)
scale.set(100)
scale.pack()

button = Button(root,
                text='submit',
                command=submit)
button.pack()

root.mainloop()
