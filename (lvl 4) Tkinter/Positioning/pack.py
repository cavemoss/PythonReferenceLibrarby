# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> pack
from tkinter import *


# instance 1
root = Tk()
root.geometry('220x220+100+100')
root.title('pack')

Button(master=root, text='a Thing 1').pack()
Button(master=root, text='a Thing 2').pack()
Button(master=root, text='a Thing 3').pack()


# instance 2
win1 = Toplevel()
win1.geometry('220x220+400+100')
win1.title('side & anchor')

Button(master=win1, text='a Thing 1').pack(side=LEFT)
Button(master=win1, text='a Thing 2').pack(anchor=E)
Button(master=win1, text='a Thing 3').pack()


# instance 3
win2 = Toplevel()
win2.geometry('220x220+700+100')
win2.title('before')

thing_one = Button(master=win2, text='a Thing 1')
thing_one.pack()
Button(master=win2, text='a Thing 2').pack(before=thing_one)


# instance 4
win3 = Toplevel()
win3.geometry('220x220+1000+100')
win3.title('padding')

Button(master=win3, text='a Thing 1').pack(pady=30, padx=30, ipadx=30, ipady=30)


# instance 5
win4 = Toplevel()
win4.geometry('220x220+1300+100')
win4.title('expand & fill')

Button(master=win4, text='a Thing 1').pack(expand=True, fill=Y)
Button(master=win4, text='a Thing 2').pack(expand=True, fill=X)
Button(master=win4, text='a Thing 3').pack(expand=True, fill=BOTH)


root.mainloop()
