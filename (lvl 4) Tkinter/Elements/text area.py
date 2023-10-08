# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GUI text area
from tkinter import *


def submit():
    input = text_area.get('1.0', END)
    print(input)


root = Tk()

text_area = Text(root,
                 height=8,
                 width=20,
                 bg='#ffffff',
                 fg='purple',
                 font=('Consolas', 16),
                 padx=20,
                 pady=20)
text_area.pack()

Button(root, text='submit', font=('Consolas', 10), command=submit).pack()

root.mainloop()
