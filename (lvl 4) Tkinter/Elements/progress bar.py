# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GUI progress bar
from tkinter import *
from tkinter.ttk import *
import time


def start():
    amount = 100
    downloaded = 0
    speed = 1

    while downloaded < amount:
        time.sleep(0.05)

        bar['value'] += (speed / amount) * 100
        downloaded += speed

        percent.set(str(int((downloaded / amount) * 100)) + '%')
        text.set(str(downloaded) + '/' + str(amount) + ' GB downloaded')

        root.update_idletasks()


root = Tk()

bar = Progressbar(root, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percent = StringVar()
Label(root, textvariable=percent).pack()

text = StringVar()
Label(root, textvariable=text).pack()

Button(root, text='Download', command=start).pack()

root.mainloop()
