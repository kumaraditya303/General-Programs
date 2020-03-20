__author__ = "Kumar Aditya"
import tkinter as tk
from tkinter import *
from tkinter.messagebox import *

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="9304554856a",
    auth_plugin='mysql_native_password',
    database="mydatabase"
)
global cursor
cursor = db.cursor()


def save():
    uname = str(username.get())
    pswd = str(password.get())
    eml = str(email.get())
    ph = str(phone.get())
    gd = str(gender.get())
    g = ''
    if(gd == "1"):
        g = 'M'
    elif(gd == "2"):
        g = 'F'
    sql = "INSERT INTO data (username,email,password,gender,phone) VALUE (%s,%s,%s,%s,%s)"
    var = (uname, eml, pswd, g, ph)
    cursor.execute(sql, var)
    db.commit()
    showinfo("Data Server", "Data Saved Successfully.")
    uname = ""
    pswd = ""
    eml = ""
    ph = ""
    gd = ""
    g = ""


gui = Tk()
gui.geometry("500x200")
gui.title("Data Collector")
username = StringVar()
password = StringVar()
email = StringVar()
gender = StringVar()
phone = StringVar()
Label(gui, text="Enter your Username:").grid(row=0, column=0)
Entry(gui, textvariable=username).grid(row=0, column=1)

Label(gui, text="Enter your Password:").grid(row=1, column=0)
Entry(gui, textvariable=password).grid(row=1, column=1)

Label(gui, text="Choose Your Gender:").grid(row=2, column=0)
Radiobutton(gui, text="Male", value="1", variable=gender).grid(row=2, column=1)
Radiobutton(gui, text="Female", value="2",
            variable=gender).grid(row=2, column=2)

Label(gui, text="Enter your Email:").grid(row=3, column=0)
Entry(gui, textvariable=email).grid(row=3, column=1)

Label(gui, text="Enter your Phone number:").grid(row=4, column=0)
Entry(gui, textvariable=phone).grid(row=4, column=1)

Button(gui, text="Save", command=save).grid(row=5, column=1)
gui.update_idletasks()
gui.mainloop()
