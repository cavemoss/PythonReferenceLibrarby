# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> OS file saving
from tkinter import *
from tkinter import filedialog


def savefile():
    file = filedialog.asksaveasfile(initialdir='C:\\Users\\alexs\\Desktop\\knowledge\\Programming\\Python\\trash',
                                    title='Save the file',
                                    defaultextension='.txt',
                                    filetypes=[
                                        ('text file', '*.txt'),
                                        ('HTML file', '*.html'),
                                        ('all files', '*.*')
                                    ])
    if file is None:
        return

    file_text = str(text_area.get(1.0, END))
    # file_text = input('enter something: ')
    file.write(file_text)
    file.close()


root = Tk()

Button(root, text='save', command=savefile).pack()

text_area = Text(root)
text_area.pack()

root.mainloop()
