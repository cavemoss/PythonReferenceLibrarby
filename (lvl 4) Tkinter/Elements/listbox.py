# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GUI listbox
from tkinter import *


def submit():
    # print('give me ' + listbox.get(listbox.curselection()))
    submitted_items = []
    print('give me ', end=' ')
    for index in listbox.curselection():
        submitted_items.insert(index, listbox.get(index))
    for index in submitted_items:
        print(index, end='  ')
    print('\n')


def add():
    listbox.insert(listbox.size(), entry_box.get())


def delete():
    # listbox.delete(listbox.curselection())
    for index in reversed(listbox.curselection()):
        listbox.delete(index)


root = Tk()
root.geometry('420x420')

listbox = Listbox(root,
                  selectmode=MULTIPLE,
                  bg='#f7ffde',
                  font=('Constantia', 30),
                  width=12)
listbox.config(height=listbox.size())

listbox_items = {1: 'sandwich',
                 2: 'salt',
                 3: 'butter',
                 4: 'cheese',
                 5: 'salad', }
for key, value in listbox_items.items():
    listbox.insert(key, value)

listbox.pack()

entry_box = Entry(root)
entry_box.pack()

submit_button = Button(root, text='submit', command=submit)
submit_button.pack()

add_button = Button(root, text='add', command=add)
add_button.pack()

delete_button = Button(root, text='delete', command=delete)
delete_button.pack()

root.mainloop()
