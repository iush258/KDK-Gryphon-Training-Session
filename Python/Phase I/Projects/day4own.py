import requests , streamlit as st
from dotenv import load_dotenv
import os 
load_dotenv()
API_KEY=os.getenv("Weather_API_KEY")


name=input("Enter City name:")
city= requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid={API_KEY}&units=metric")

data = city.json()
print(data)
# print(f"temperature in {name} is {data["main"]["temp"]}")
# print(f"it feels like: {data["main"]["feels_like"]}")
# print(f"Minimum temperature in {name} is {data["main"]["temp_min"]}")
# print(f"Maxsimum temperature in {name} is {data["main"]["temp_max"]}")
# print(f"Pressure  in {name} is {data["main"]["pressure"]}")
# print(f"Humidity in {name} is {data["main"]["humidity"]}")
# print(f"Sea Level from {name} is {data["main"]["sea_level"]}")
# print(f"Ground level {name} is {data["main"]["grnd_level"]}")

