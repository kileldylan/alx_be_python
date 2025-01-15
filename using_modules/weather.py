# script to fetch weather data from the API and display it

import requests

API_KEY = '096a8380d7c120c3f056b2a5ba85412c'

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def weather_data():
    city = input("Enter the city name: ")
    url = f"{BASE_URL}?q={city}&appid={API_KEY}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        
        if 'main' in data:
            temp_kelvin = data['main']['temp']
            temp_celsius = kelvin_to_celsius(temp_kelvin)
            print(f"The temperature in {city} is {temp_celsius:.2f}°C")
        else:
            print(f"Could not retrieve weather data for {city}.")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

weather_data()