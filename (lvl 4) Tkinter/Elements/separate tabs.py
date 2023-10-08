# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GUI separate tabs
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('420x420')

notebook = ttk.Notebook(root)
tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text='TAB1')
notebook.add(tab2, text='TAB2')
notebook.pack(expand=True, fill='both')

Label(tab1, text='welcome to tab 1', width=50, height=25).pack()
Label(tab2, text='welcome to tab 2', width=50, height=25).pack()

root.mainloop()
