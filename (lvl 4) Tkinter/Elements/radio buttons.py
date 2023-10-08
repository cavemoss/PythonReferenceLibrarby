# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GUI radio buttons
from tkinter import *


def how_feel():
    if x.get() == 0:
        print('you are sadge(')
    elif x.get() == 1:
        print('you are happy))')
    elif x.get() == 2:
        print('you are angyyyy!!')
    else:
        print('huh?')


root = Tk()

sadge = PhotoImage(file='(path)\\sadge_abby.gif')
angy = PhotoImage(file='(path)\\angy_abby.gif')
happy = PhotoImage(file='(path)\\happy_abby.gif')

emotions = ['sadge', 'happy', 'angy']
emotion_images = [sadge, happy, angy]

x = IntVar()
for index in range(len(emotions)):
    radio_button = Radiobutton(root,
                               text=emotions[index],

                               variable=x,
                               value=index,
                               command=how_feel,

                               padx=25,
                               font=('Impact', 16),

                               image=emotion_images[index],
                               anchor=W,
                               compound='left',

                               indicatoron=False,
                               width=211)
    radio_button.pack(anchor=W)

root.mainloop()
