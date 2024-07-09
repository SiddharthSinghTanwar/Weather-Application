from flask import Flask, request, render_template
from weather import get_weather
from waitress import serve
from pprint import pprint

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET', 'POST'])
def weather():

    city = request.args.get('city')
    # print(city)

    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        print('City name is empty')
        return render_template('city_not_found.html')          

    weather_data = get_weather(city)
    # print("*** Current weather data ***")
    # pprint(weather_data)

    try:
        if weather_data['error']['code'] == 1006:
            # print('City not found')
            return render_template('city_not_found.html')
    except KeyError:
        pass
    # if weather_data['current']['condition']['code'] == 200:
    #     print('City not found')
    #     return render_template('city_not_found.html')
    
    return render_template('weather.html',
                            title=weather_data['location']['name'],
                            temp=weather_data['current']['temp_c'],
                            feels_like=weather_data['current']['feelslike_c'])
    
    # return render_template('weather.html')
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)