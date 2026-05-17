# 🌤️ Weather Dashboard with Flask

A web app that displays real-time weather data for any city, built with Python and Flask and hosted on PythonAnywhere.

🌐 **Live Site:** [abdulhadicoder.pythonanywhere.com](https://abdulhadicoder.pythonanywhere.com)

## 📋 Features

- Search weather by city name
- Displays temperature, feels like, humidity, and wind speed
- Friendly error message for invalid city names

## 🛠️ Built With

- **Python 3** – backend logic
- **Flask** – web framework
- **HTML5 & CSS3** – frontend
- **OpenWeatherMap API** – weather data

## 📁 Project Structure
Weather-Dashboard-with-Flask/
│
├── static/          # CSS styles
├── templates/       # HTML templates
├── app.py           # Main Flask application
├── requirements.txt # Python dependencies
└── Procfile         # Deployment config

## 🚀 Run Locally

```bash
git clone https://github.com/abdulhadiasifhassan-coder/Weather-Dashboard-with-Flask.git
cd Weather-Dashboard-with-Flask
pip install -r requirements.txt
```

Create a `config.ini` file with your API key:
```ini
[openweathermap]
api = YOUR_API_KEY
```

Then run:
```bash
python app.py
```

## 📌 Data Source

Weather data sourced from [OpenWeatherMap API](https://openweathermap.org/api).