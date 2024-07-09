import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()


def get_current_weather():
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name:\n")

    request_url = f"https://api.weatherapi.com/v1/current.json?key={os.getenv("API_KEY")}&q={city}"

    # print(request_url)

    weather_data = requests.get(request_url).json()

    pprint(weather_data)

    print(f'\nCurrent weather for {weather_data["location"]['name']}:')
    print(f'\nThe temp is {weather_data["current"]["temp_c"]:.1f}°')
    print(
        f'\nBut it feels like {weather_data["current"]["feelslike_c"]:.1f}°\n')


if __name__ == "__main__":
    get_current_weather()