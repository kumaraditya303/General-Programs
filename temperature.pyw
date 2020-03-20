import tkinter
from tkinter import *
gui = Tk()
gui.title("GUI Temperature Converter")
gui.configure(bg="#000000")
gui.minsize(400, 300)
gui.resizable(height=False, width=False)
var = IntVar()
chg = IntVar()
a = StringVar()
b = StringVar()
c = StringVar()


def sel():
    x = int(var.get())
    return x


def answer():
    temp = float(E1.get())
    v = sel()
    t = int(chg.get())
    if(v == 1 and t == 1):
        a1 = temp
    elif(v == 1 and t == 2):
        a1 = temp*9/5+32
    elif(v == 1 and t == 3):
        a1 = temp+273.15
    elif(v == 2 and t == 1):
        a1 = (temp-32)*5/9
    elif(v == 2 and t == 2):
        a1 = temp
    elif(v == 2 and t == 3):
        a1 = (temp-32)*5/9+273.15
    elif(v == 3 and t == 1):
        a1 = temp-273.15
    elif(v == 3 and t == 2):
        a1 = (temp-273.15)*9/5+32
    elif(v == 3 and t == 3):
        a1 = temp
    a1 = round(a1, 2)
    a.set(str(a1))


L1 = Label(gui, text="Convert From: ", bg="#000000",
           fg="#FFFFFF", font="Ubuntumono").place(x=10, y=10)
R1 = Radiobutton(gui, text="Celsius", variable=var, value=1, bg="#000000", fg="#FFFFFF", font="Ubuntumono",foreground="red",
                 command=sel).place(x=10, y=50)

R2 = Radiobutton(gui, text="Fahrenheit", variable=var, value=2,
                 command=sel, bg="#000000", fg="#FFFFFF", font="Ubuntumono",foreground="red").place(x=120, y=50)

R3 = Radiobutton(gui, text="Kelvin", variable=var, value=3,
                 command=sel, bg="#000000", fg="#FFFFFF", font="Ubuntumono",foreground="red").place(x=250, y=50)
L2 = Label(gui, text="Enter Temperature: ", bg="#000000",
           fg="#FFFFFF", font="Ubuntumono").place(x=10, y=90)
E1 = Entry(gui)
E1.place(x=200, y=90)
L3 = Label(gui, text="________________________________________________________________________________________________________________________________________________________________________________",
           bg="#000000", fg="#FFFFFF", font="Ubuntumono").place(x=0, y=110)
L4 = Label(gui, text="Convert To: ", bg="#000000",
           fg="#FFFFFF", font="Ubuntumono").place(x=10, y=130)
R4 = Radiobutton(gui, text="Celsius", variable=chg, value=1,
                 command=answer, bg="#000000", fg="#FFFFFF", font="Ubuntumono",foreground="red").place(x=10, y=170)

R5 = Radiobutton(gui, text="Fahrenheit", variable=chg, value=2,
                 command=answer, bg="#000000", fg="#FFFFFF", font="Ubuntumono",foreground="red").place(x=120, y=170)

R6 = Radiobutton(gui, text="Kelvin", variable=chg, value=3,
                 command=answer, bg="#000000", fg="#FFFFFF", font="Ubuntumono",foreground="red").place(x=250, y=170)

L5 = Label(gui, text="Converted Temperature: ", bg="#000000",
           fg="#FFFFFF", font="Ubuntumono").place(x=10, y=210)
L6 = Label(gui, textvariable=a, bg="#000000", fg="#FFFFFF",
           font="Ubuntumono").place(x=200, y=210)
gui.update_idletasks()
gui.mainloop()
