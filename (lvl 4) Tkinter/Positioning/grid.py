# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> grid
from tkinter import *


# instance 1
root = Tk()
root.geometry('220x220+100+100')
root.title('grid')

Button(master=root, text='a Thing 1').grid(row=0, column=0)
Button(master=root, text='a Thing 2').grid(row=0, column=1)
Button(master=root, text='a Thing 3').grid(row=1, column=0, columnspan=2)
Button(master=root, text='a Thing 4').grid(row=0, column=2, rowspan=2)


# instance 2
win1 = Toplevel()
win1.geometry('220x220+400+100')
win1.title('grid sticky')

Button(master=win1, text='a Thing 1').grid(row=0, column=0)
Button(master=win1, text='a Thing 2').grid(row=0, column=1)
Button(master=win1, text='a Thing 3').grid(row=1, column=0, columnspan=2, sticky='e')
Button(master=win1, text='a Thing 4').grid(row=0, column=2, rowspan=2, sticky='s')


# instance 3
win2 = Toplevel()
win2.geometry('220x220+700+100')
win2.title('configure weight')

win2.rowconfigure(1, weight=1)
win2.columnconfigure(2, weight=1)

Button(master=win2, text='a Thing 1').grid(row=0, column=0)
Button(master=win2, text='a Thing 2').grid(row=0, column=1)
Button(master=win2, text='a Thing 3').grid(row=1, column=0, columnspan=2, sticky='ns')
Button(master=win2, text='a Thing 4').grid(row=0, column=2, rowspan=2, sticky='ew')


# instance 4
win3 = Toplevel()
win3.geometry('220x220+1000+100')
win3.title('padding')

win3.rowconfigure(0, weight=1)
win3.columnconfigure(0, weight=1)

Button(master=win3, text='a Thing 1').grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
Button(master=win3, text='a Thing 2').grid(row=0, column=1)
Button(master=win3, text='a Thing 3').grid(row=1, column=0)


# instance 5
win4 = Toplevel()
win4.geometry('220x220+1300+100')
win4.title('configure coefficient')

win4.rowconfigure(0, weight=5)
win4.rowconfigure(1, weight=1)
win4.columnconfigure(0, weight=1)

Button(master=win4, text='a Thing 1').grid(row=0, column=0, sticky='nsew')
Button(master=win4, text='a Thing 2').grid(row=1, column=0, sticky='nsew')


root.mainloop()
