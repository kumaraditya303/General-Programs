from tkinter import *
import tkinter as tk
gui = Tk()
gui.title("GUI Quadratic Solver")
gui.configure(bg="#000000",)
gui.minsize(600,400)
ansp = StringVar()
ansn = StringVar()
equation = StringVar()


def sign(x):
    if(x >= 0):
        return "+"
    elif(x < 0):
        return "-"


def answer():

    ax = float(eval(e1.get().replace("^","**")))
    bx = float(eval(e2.get().replace("^","**")))
    c = float(eval(e3.get().replace("^","**")))

    if(abs(ax) == 1 and abs(bx) == 1):
        eq = "x\N{SUPERSCRIPT TWO} " + \
            sign(bx)+" x "+sign(c) + str(abs(c))+" = 0"
    else:
        eq = str(ax)+"x\N{SUPERSCRIPT TWO} "+sign(bx) + \
            str(abs(bx))+"x "+sign(c) + str(abs(c))+" = 0"
    pans = ((-bx+(bx**2-4*ax*c)**(1/2))/(2*ax))
    nans = ((-bx-(bx**2-4*ax*c)**(1/2))/(2*ax))
    pans = str(pans).replace("j", "i")
    nans = str(nans).replace("j", "i")
    equation.set(eq)
    ansp.set(pans)
    ansn.set(nans)



l1 = Label(gui, text="Enter the coefficient of x\N{SUPERSCRIPT TWO}: ",
           bg="#000000", fg="#FFFFFF", font="Ubuntumono")
l1.place(x=10, y=10)
e1 = Entry(gui, bd=2, bg="#000000", fg="#FFFFFF", font="Ubuntumono")
e1.place(x=250, y=10)

l2 = Label(gui, text="Enter the coefficient of x: ",
           bg="#000000", fg="#FFFFFF", font="Ubuntumono")
l2.place(x=10, y=50)
e2 = Entry(gui, bd=2, bg="#000000", fg="#FFFFFF", font="Ubuntumono")
e2.place(x=250, y=50)

l3 = Label(gui, text="Enter the constant: ",
           bg="#000000", fg="#FFFFFF", font="Ubuntumono")
l3.place(x=10, y=90)
e3 = Entry(gui, bd=2, bg="#000000", fg="#FFFFFF", font="Ubuntumono")
e3.place(x=250, y=90)

l4 = Label(gui, text="First solution: ", bg="#000000",
           fg="#FFFFFF", font="Ubuntumono")
l4.place(x=10, y=130)
e4 = Label(gui, bd=2, textvariable=ansp, bg="#000000",
           fg="#FFFFFF", font="Ubuntumono")
e4.place(x=250, y=130)

l5 = Label(gui, text="Second solution: ", bg="#000000",
           fg="#FFFFFF", font="Ubuntumono")
l5.place(x=10, y=170)
e5 = Label(gui, bd=2, textvariable=ansn, bg="#000000",
           fg="#FFFFFF", font="Ubuntumono")
e5.place(x=250, y=170)

l6 = Label(gui, text="Equation:", bg="#000000",
           fg="#FFFFFF", font="Ubuntumono")
l6.place(x=10, y=210)
e6 = Label(gui, textvariable=equation, bg="#000000",
           fg="#FFFFFF", font="Ubuntumono")
e6.place(x=250, y=210)

b = Button(gui, text="Solve", command=lambda: answer(),
           bg="#000000", fg="#FFFFFF", font="Ubuntumono")
b.place(x=250, y=250)
gui.update_idletasks()
gui.mainloop()
