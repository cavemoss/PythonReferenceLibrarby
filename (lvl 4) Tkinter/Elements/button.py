# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GUI button
from tkinter import *

count = 0


def click():
    global count
    count += 1
    print('why did you do that?', count)


root = Tk()

root.geometry('420x420')
root.config(background='Blue')
root.title('GUI')

photo = PhotoImage(file='(path)\\picture.png')

button = Button(root,
                command=click,
                state=ACTIVE,

                text='dont click this',
                font=('Comic Sans', 30),

                fg='#00ff00',
                bg="black",
                activeforeground='red',
                activebackground='#e04646',

                image=photo,
                compound='top')
button.pack()

root.mainloop()
