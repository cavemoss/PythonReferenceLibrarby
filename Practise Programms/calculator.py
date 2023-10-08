from tkinter import *

def button_press(num):

    global equation_text
    print(num)
    equation_text = equation_text +str(num)
    equation_label.set(equation_text)

def equals():
    
    global equation_text
    try:
        total =str(eval(equation_text))
        equation_label.set(total)
    except Exception as error:
        equation_text =''
        equation_label.set('error')
    equation_text =total

def clear():

    global equation_text
    equation_label.set('')
    equation_text =''

root =Tk()
root.title('calculator')
root.geometry('500x600')

equation_text =str()
equation_label =StringVar()

label =Label(root, textvariable=equation_label, font=('consolas',20), bg='white', width=24, height=2)
label.pack()

frame =Frame(root)
frame.pack()

buttons1 =Button(frame, text='1', height=4, width=9, font=35, command= lambda: button_press('1'))
buttons2 =Button(frame, text='2', height=4, width=9, font=35, command= lambda: button_press('2'))
buttons3 =Button(frame, text='3', height=4, width=9, font=35, command= lambda: button_press('3'))
buttons4 =Button(frame, text='4', height=4, width=9, font=35, command= lambda: button_press('4'))
buttons5 =Button(frame, text='5', height=4, width=9, font=35, command= lambda: button_press('5'))
buttons6 =Button(frame, text='6', height=4, width=9, font=35, command= lambda: button_press('6'))
buttons7 =Button(frame, text='7', height=4, width=9, font=35, command= lambda: button_press('7'))
buttons8 =Button(frame, text='8', height=4, width=9, font=35, command= lambda: button_press('8'))
buttons9 =Button(frame, text='9', height=4, width=9, font=35, command= lambda: button_press('9'))
buttons0 =Button(frame, text='0', height=4, width=9, font=35, command= lambda: button_press('0'))

buttons1.grid(row=0, column=0)
buttons2.grid(row=0, column=1)
buttons3.grid(row=0, column=2)
buttons4.grid(row=1, column=0)
buttons5.grid(row=1, column=1)
buttons6.grid(row=1, column=2)
buttons7.grid(row=2, column=0)
buttons8.grid(row=2, column=1)
buttons9.grid(row=2, column=2)
buttons0.grid(row=3, column=1)

plus =Button(frame, text='+', height=4, width=9, font=35, command= lambda: button_press('+'))
plus.grid(row=0, column=3)

minus =Button(frame, text='-', height=4, width=9, font=35, command= lambda: button_press('-'))
plus.grid(row=1, column=3)

mult =Button(frame, text='*', height=4, width=9, font=35, command= lambda: button_press('*'))
mult.grid(row=2, column=3)

div =Button(frame, text='/', height=4, width=9, font=35, command= lambda: button_press('/'))
div.grid(row=3, column=3)

equal =Button(frame, text='=', height=4, width=9, font=35, command= equals)
equal.grid(row=3, column=2)

decimal =Button(frame, text='.', height=4, width=9, font=35, command= lambda: button_press('.'))
decimal.grid(row=3, column=0)

clearb =Button(root, text='clear', height=3, width=25, font=35, command= clear)
clearb.pack()

root.mainloop()