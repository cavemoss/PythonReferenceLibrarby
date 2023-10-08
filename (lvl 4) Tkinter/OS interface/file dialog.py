# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> OS file dialog
from tkinter import *
from tkinter import filedialog


def openfile():
    path = filedialog.askopenfilename(initialdir='C:\\Users\\alexs\\Desktop\\knowledge\\Programming\\Python',
                                      title='Open a file',
                                      filetypes=(('text files', '*.txt'),
                                                 ('all files', '*.*'))
                                      )
    if path == '':
        return

    file = open(path, 'r')
    print(file.read())
    file.close()

root = Tk()

Button(root, text='Open', font=('Consolas', 14), command=openfile).pack()

root.mainloop()
