# 🌤️ Weather Dashboard with Flask

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![PythonAnywhere](https://img.shields.io/badge/Hosted%20on-PythonAnywhere-1D9FD7?style=flat)

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
```
Weather-Dashboard-with-Flask/
│
├── static/          # CSS styles
├── templates/       # HTML templates
├── app.py           # Main Flask application
└── requirements.txt # Python dependencies
```
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
