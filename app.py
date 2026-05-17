import configparser
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def weather_dashboard():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def render_results():
    city = request.form['city']
    api_key = get_api_key()
    data = get_weather_results(city, api_key)

    if data.get("cod") != 200:
        error_message = "City not found. Please check the name and try again."
        return render_template('index.html', error=error_message)

    temp = "{0:.2f}".format(data["main"]["temp"])
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    humidity = "{0:.2f}".format(data["main"]["humidity"])
    wind_speed = "{0:.2f}".format(data["wind"]["speed"])
    location = data["name"]

    return render_template('results.html', location=location, temp=temp,
                           feels_like=feels_like, weather=weather,
                           humidity=humidity, wind_speed=wind_speed)

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def get_weather_results(city, api_key):
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    r = requests.get(api_url)
    return r.json()

if __name__ == '__main__':
    app.run()