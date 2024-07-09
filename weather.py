from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_weather(name='Jaipur'):
    request_url = f"https://api.weatherapi.com/v1/current.json?key={os.getenv("API_KEY")}&q={name}"
    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print('\n ***Get current weather data*** \n')
    name = input('Enter city name: ')
    weather_data = get_weather(name)
    print(f"Current weather in {name}:")
    pprint(weather_data)