# weather_app
 
### Description
This is a web application with API. Shows the current weather in a specific city.
[All weather data from here.](https://openweathermap.org/)
****
### How to run
You need:
* Clone this repository. `clone https://github.com/Nastya67/weather_app.git`
* Create file ../weather_app/model/secret.py. Write there `API_KEY = "{your_api_key}"`
 > You can generate own API on https://openweathermap.org/ .
* Install all requirements. `pip install -r requirements.txt`
* Open terminal in project folder. Run command `python manage.py run`
* *You can use it on http://127.0.0.1:5000/*
****
### Project structure
|weather_app
|---api
|------__init__.py
|------errors.py
|------views.py
|------WeatherResponse.py
|---app
|------__init__.py
|------errors.py
|------views.py
|------WeatherResponse.py
|---model
|------InputValidator.py
|------secret.py
|------WeatherExceptions.py
|------WeatherModel.py
|------WeatherRepository.py
|---templates
|------404.html
|------500.html
|------index.html
|---__init__.py
|-



***
### API