# Simple GUI Calculator BY Kumar Aditya
import tkinter as tk
from tkinter import *
import time
expression = ""


def press(num):
    global expression
    expression += str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set(" Error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


gui = Tk()
gui.configure(background="light blue")
gui.title("Simple GUI Calculator")
equation = StringVar()
expression_block = Label(gui, textvariable=equation,
                         font="Cascadia", bg="#FFFFFF", fg="#000000")
expression_block.grid(columnspan=4, ipadx=100, ipady=30)
button1 = Button(gui, text=' 1 ', fg='black', bg='red',
                 command=lambda: press(1), height=3, width=7, font="Cascadia")
button1.grid(row=2, column=0)

button2 = Button(gui, text=' 2 ', fg='black', bg='red',
                 command=lambda: press(2), height=3, width=7, font="Cascadia")
button2.grid(row=2, column=1)

button3 = Button(gui, text=' 3 ', fg='black', bg='red',
                 command=lambda: press(3), height=3, width=7, font="Cascadia")
button3.grid(row=2, column=2)

button4 = Button(gui, text=' 4 ', fg='black', bg='red',
                 command=lambda: press(4), height=3, width=7, font="Cascadia")
button4.grid(row=3, column=0)

button5 = Button(gui, text=' 5 ', fg='black', bg='red',
                 command=lambda: press(5), height=3, width=7, font="Cascadia")
button5.grid(row=3, column=1)

button6 = Button(gui, text=' 6 ', fg='black', bg='red',
                 command=lambda: press(6), height=3, width=7, font="Cascadia")
button6.grid(row=3, column=2)

button7 = Button(gui, text=' 7 ', fg='black', bg='red',
                 command=lambda: press(7), height=3, width=7, font="Cascadia")
button7.grid(row=4, column=0)

button8 = Button(gui, text=' 8 ', fg='black', bg='red',
                 command=lambda: press(8), height=3, width=7, font="Cascadia")
button8.grid(row=4, column=1)

button9 = Button(gui, text=' 9 ', fg='black', bg='red',
                 command=lambda: press(9), height=3, width=7, font="Cascadia")
button9.grid(row=4, column=2)

button0 = Button(gui, text=' 0 ', fg='black', bg='red',
                 command=lambda: press(0), height=3, width=7, font="Cascadia")
button0.grid(row=5, column=0)

button00 = Button(gui, text=' . ', fg='black', bg='red',
                  command=lambda: press("."), height=3, width=7, font="Cascadia")
button00.grid(row=5, column=1)

plus = Button(gui, text=' + ', fg='black', bg='red',
              command=lambda: press("+"), height=3, width=7, font="Cascadia")
plus.grid(row=2, column=3)

minus = Button(gui, text=' - ', fg='black', bg='red',
               command=lambda: press("-"), height=3, width=7, font="Cascadia")
minus.grid(row=3, column=3)

multiply = Button(gui, text=' * ', fg='black', bg='red',
                  command=lambda: press("*"), height=3, width=7, font="Cascadia")
multiply.grid(row=4, column=3)

divide = Button(gui, text=' / ', fg='black', bg='red',
                command=lambda: press("/"), height=3, width=7, font="Cascadia")
divide.grid(row=5, column=3)

exp = Button(gui, text=' ^ ', fg='black', bg='red',
             command=lambda: press("**"), height=3, width=7, font="Cascadia")
exp.grid(row=6, column=0)

percent = Button(gui, text=' % ', fg='black', bg='red',
                 command=lambda: press("*0.01"), height=3, width=7, font="Cascadia")
percent.grid(row=6, column=1)

pi = Button(gui, text=' π ', fg='black', bg='red',
            command=lambda: press("22/7"), height=3, width=7, font="Cascadia")
pi.grid(row=6, column=2)

equal = Button(gui, text=' = ', fg='black', bg='red',
               command=equalpress, height=3, width=7, font="Cascadia")
equal.grid(row=5, column=2)

clear = Button(gui, text='Clear', fg='black', bg='red',
               command=clear, height=3, width=7, font="Cascadia")
clear.grid(row=6, column=3)
gui.mainloop()