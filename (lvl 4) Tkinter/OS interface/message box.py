# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> OS message box
from tkinter import *
from tkinter import messagebox


import threading
import time
stop = False
def break_function():
    global stop
    time.sleep(10)
    stop = True


def click():
    messagebox.showinfo(title='info for you', message='you are a cutie :3')

    messagebox.showerror(message='something\'s off')

    messagebox.showwarning(title='warning', message='I SEE YOU')
    threading.Thread(target=break_function).start()
    while True:
        if stop is False:
            messagebox.showwarning(title='warning', message='AM COMING FOR YOU')
        else:
            break

    if messagebox.askokcancel(message='Do you wont to do the thing?') is True:
        print('you did the thing')
    else:
        print('you didn\'t do the thing')

    if messagebox.askretrycancel(message='Do you wont to retry the thing?') is True:
        print('you retried the thing')
    else:
        print('you didn\'t retry the thing')

    if messagebox.askyesno(title='cake', message='Do you like cake?') is True:
        print('me too!')
    else:
        print('ahh((')

    answer = messagebox.askquestion(title='cake 2.0', message='Do you like cake?')
    if answer == 'yes':
        print('me too!')
    else:
        print('me neither!')

    reply = messagebox.askyesnocancel(title='cake 3.0', message='Do you like cake?')
    if reply is True:
        print('me too!')
    elif reply is False:
        print('me neither!') 
    else:
        print('you withheld the answer')

    messagebox.showinfo(title='info for you', message='you are a cutie :3', icon='warning')

root = Tk()

button = Button(root, text='click this now!', command=click)
button.pack()

root.mainloop()
