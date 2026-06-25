import requests , streamlit as st
#
API_KEY="ca686571cfc1fe0a387124e63bc9fdd0"
def findwe(nm):
    a=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={nm}&appid={API_KEY}&units=metric")
    try:
        if a.status_code==200:
            data=a.json()
            return data

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

        st.write(f"Temperature in {name} is {data["main"]["temp"]}℃")
        st.write(f"It feels like: {data["main"]["feels_like"]}")
        st.write(f"Minimum temperature in {name} is {data["main"]["temp_min"]} ℃")
        st.write(f"Maximum temperature  in {name} is {data["main"]["temp_max"]}℃")
        st.write(f"Pressure  in {name} is {data["main"]["pressure"]}")
        st.write(f"Humidity in {name} is {data["main"]["humidity"]}")
        st.write(f"Sea Level from {name} is {data["main"]["sea_level"]}")
        st.write(f"Ground level {name} is {data["main"]["grnd_level"]}")
except TypeError:
    st.write("Enter Proper Name!!!")
