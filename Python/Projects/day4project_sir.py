import requests , streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY=os.getenv("Weather_API_KEY")



def findwe(nm):
    a=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={nm}&appid={API_KEY}&units=metric")
    try:
        if a.status_code==200:
            data=a.json()
            st.success("Weather Fetched Sucessfully!")
            return data
        else:
            st.error("Enter Correct City Name")

    except TypeError:
        st.write("Enter Proper Name!!!")




#main
st.set_page_config(
    page_title="Day 4 Project",
    page_icon=":sunny:"
    
)
st.title("Weather App Using Weather Api")
st.write("Enter the city name to get the weather information")
name=st.text_input("Enter City Name:")


try:
    if st.button("Find Weather"):
        data=findwe(name)
        st.subheader(f"{data["name"]},{data["sys"]["country"]}")
        col1,col2,col3,col4=st.columns(4)
        col5,col6,col7,col8=st.columns(4)
        col9,col10,col11,col12 = st.columns(4)

        col1.metric("Main",f"{data["weather"][0]["main"]}")
        col2.metric("Temperature",f"{data["main"]["temp"]}℃")
        col3.metric("It Feels Like",f"{data["main"]["feels_like"]}")
        col4.metric("Minimum Temperature",f"{data["main"]["temp_min"]}℃")
        col5.metric("Maximum Temperature",f"{data["main"]["temp_max"]}℃")
        col6.metric("Pressure",f"{data["main"]["pressure"]}Pa")
        col7.metric("Humidity",f"{data["main"]["humidity"]}")
        col8.metric("Sea level",f"{data["main"]["sea_level"]}m")
        col9.metric("Ground Level",f"{data["main"]["grnd_level"]}m")
except TypeError:
    print("Error Handled")


