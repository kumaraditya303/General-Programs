import requests
import json
import os
os.system('cls')
url = "http://api.openweathermap.org/data/2.5/weather?q=Patna,in&APPID=e53f4e88de7c733cd0cb37bb6c117e94"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    pressure = data['main']["pressure"]
    humidity = data['main']["humidity"]
    wind_speed = data["wind"]["speed"]
    wind_degree = data["wind"]["deg"]

    print(f"Temperature = {temp}°C")
    print(f"Humidity = {humidity} %")
    print(f"Pressure = {pressure} bar")
    print(f"Wind speed = {wind_speed} m/s")
    print(f"Wind degree = {wind_degree}°")
