#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#drag and drop widget

def dragstart(event):
    widget =event.widget
    widget.startX =event.x
    widget.startY =event.y

def dragmotion(event):
    widget =event.widget
    x=widget.winfo_x() - widget.startX + event.x
    y=widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

from tkinter import *


root =Tk()

label =Label(root, bg='red', width=10, height=5)
label.place(x=0,y=0)
label.bind('<Button-1>',dragstart)
label.bind('<B1-Motion>',dragmotion)

label2 =Label(root, bg='blue', width=10, height=5)
label2.place(x=10,y=10)
label2.bind('<Button-1>',dragstart)
label2.bind('<B1-Motion>',dragmotion)

root.mainloop()