# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GUI label
from tkinter import *

root = Tk()

root.geometry('1080x420')
root.config(background='Blue')
root.title('GUI')

photo = PhotoImage(file='(path)\\happy_abby.gif')

label = Label(root,
              text='happyhappyhappyhappyhappy',
              font=('Arial', 40, 'bold'),

              fg='#DDDFFF',
              bg='red',
              relief=RAISED,

              bd=10,
              padx=20,
              pady=20,

              image=photo,
              compound='bottom')

label.pack()
# label.place(x=0,y=0)

root.mainloop()
