import datetime 
import json
import requests

# https://api.openweathermap.org/data/2.5/weather?q={city}&appid={your_api_key}


# Searches the weather takes two parameter as input city api key
def fetch_weather(city,api_key):

    # Generating url with the featched api key and the city entered by the user
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL = BASE_URL + "q=" + city +"&appid=" + api_key

    # Requesting for the json file
    try:
        response = requests.get(URL)

        # check if the json file was sucessfully retrived 
        if response.status_code == 200:
            # Parsing the json file
            json_response = response.json()
            return json_response
        else:
           return f"Error {response.status_code}, Please check the city name you entered and try again."

    except requests.exceptions.RequestException as e:
        return f"Error occured{e}"
        
def display_weather(weather_data):
    if weather_data:
        city = weather_data["name"]
        country = weather_data["sys"]["country"]
        temperature = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]
        humidity = weather_data["main"]["humidity"]
        condition = weather_data["weather"][0]["main"]
        condition_description = weather_data["weather"][0]["description"]
        wind_speed = weather_data["wind"]["speed"]
        sunrise_unixtime = weather_data["sys"]["sunrise"]
        sunset_unixtime = weather_data["sys"]["sunset"]
        

        # Converting unix_timestamp in human readable format
        sunrise_time = datetime.datetime.fromtimestamp(sunrise_unixtime).strftime('%H:%M:%S')
        sunset_time = datetime.datetime.fromtimestamp(sunset_unixtime).strftime('%H:%M:%S')
        return (print(f"""Weather Report for {city}, {country}:Temperature: {temperature}°K (Feels like: {feels_like}°K)
Condition: {condition} ({condition_description})
Humidity: {humidity}%
Wind Speed: {wind_speed} m/s
Sunrise: {sunrise_time}
Sunset: {sunset_time} """))
        
    else:
        return f"No weather data to display"
    
# retriving the api_key from the file
API_KEY = open("api_key.txt","r").read()

# Input from the user for the city name
CITY = input("Please enter the name of the city for which you want to check the weather:")

# Function call
data = fetch_weather(CITY,API_KEY)
weather_info = display_weather(data)