import requests
import json
import os
from tkinter import *
from tkinter.messagebox import *
from datetime import datetime
url = "http://api.openweathermap.org/data/2.5/weather?q=Patna,in&APPID=e53f4e88de7c733cd0cb37bb6c117e94"
gui = Tk()
gui.title("Current Weather")
gui.minsize(400, 400)

t = StringVar()
h = StringVar()
p = StringVar()
ws = StringVar()
wd = StringVar()
time = StringVar()


def weather():
    try:
        response = requests.get(url)
    except requests.ConnectionError:
        showwarning("Error", "Error in connecting to internet!")
        exit()

    data = response.json()
    temp = data['main']['temp']-273.15
    pressure = data['main']["pressure"]
    humidity = data['main']["humidity"]
    wind_speed = data["wind"]["speed"]
    wind_degree = data["wind"]["deg"]
    t.set(str(temp)+" °C")
    p.set(str(pressure)+" bar")
    h.set(str(humidity)+" %")
    ws.set(str(wind_speed)+" m/s")
    wd.set(str(wind_degree)+" °")
    time.set("Time = "+str(datetime.now()))
    print("Temperature = %.2f°C\r\n", temp)
    print("Humidity = %d %%\r\n", humidity)
    print("Pressure = %.3f bar\r\n", pressure)
    print("Wind speed = %.1f m/s\r\n", wind_speed)
    print("Wind degree = %d°\r\n\r\n", wind_degree)
    print("\n\n")


weather()

Label(gui, text="Temperature = ").place(x=110, y=10)
Label(gui, text="Humidity = ").place(x=110, y=50)
Label(gui, text="Pressure = ").place(x=110, y=90)
Label(gui, text="Wind speed = ").place(x=110, y=130)
Label(gui, text="Wind degree = ").place(x=110, y=170)


Label(gui, textvariable=t).place(x=250, y=10)
Label(gui, textvariable=h).place(x=250, y=50)
Label(gui, textvariable=p).place(x=250, y=90)
Label(gui, textvariable=ws).place(x=250, y=130)
Label(gui, textvariable=wd).place(x=250, y=170)
Label(gui, textvariable=time).place(x=110, y=210)
Button(gui, text="Update Weather", command=lambda: weather()).place(x=150, y=250)
gui.update_idletasks()
gui.mainloop()
