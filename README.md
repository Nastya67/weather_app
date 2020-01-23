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
|weather_app\
|---api\
|------\_\_init\_\_.py\
|------errors.py\
|------views.py\
|------WeatherResponse.py\
|---app\
|------\_\_init\_\_.py\
|------errors.py\
|------views.py\
|------WeatherResponse.py\
|---model\
|------InputValidator.py\
|------secret.py\
|------WeatherExceptions.py\
|------WeatherModel.py\
|------WeatherRepository.py\
|---templates\
|------404.html\
|------500.html\
|------index.html\
|---\_\_init\_\_.py\
|config.py\
|manage.py\
|normalized_city_names.json\
|requirements.txt

__api.views.get_weather_by_city()__ - is api controller on url ../api/. 
Accepted method is GET. GET parameters *city_name* or (*lon, lat*).\
Return: json representation of weather.\
Errors: 404 if params are incorrect.

__api.errors.error(er)__ - is api controller on 404 error. \
Args: *er* - str type. Error message.\
Return: json representation of error.

__api.WeatherResponse.WeatherApiResponse(weather)__ - JSON for the API 
response is created in this class.\
Args: *weather* - model.WeatherModel.WeatherModel type.\
Fields: *json* - dict type. JSON representation of weather.

Methods: 
* __*get_response()*__ \
Return: dict type. JSON representation of weather.

__app.views.index()__ - is controller on base url ../ .
Accepted method is GET. GET parameters *city_name* or nothing.\
Return: HTML start page with one input field.\
Redirects on: ../city_name if *city_name* is defined.

__app.views.show_city_weather(city_name)__ - is controller on url ../<city_name>.
Accepted method is GET. \
Return: HTML page with one input field and weather info in the city.\
Errors: 404 if *city_name* is incorrect.

__app.errors.page_not_found(er)__ - is api controller on 404 error. \
Args: *er* - str type. Error message.\
Return: HTML page with text of error.

__app.WeatherResponse.WeatherResponse(weather)__ - class to represent
object of weather as on front. \
Args: *weather* - model.WeatherModel.WeatherModel type.\
Fields: 
* *city_name* - str type. Name of city where is the weather.
* *date* - datetime.date type. Date of weather, UTC.
* *temp* - float type. Temperature, Celsius.
* *pressure* - float type. Atmospheric pressure, hPa. 
* *humidity* - float type. Humidity, %.
* *wind_speed* - float type. Wind speed, meter/sec.
* *wind_deg* - float type. Wind direction, degrees.
* *visibility* - int type or None. Visibility, meter.
* *clouds* - float type. Cloudiness, %.
* *sunrise* - datetime.time type. Sunrise time, UTC.
* *sunset* - datetime.time type. Sunset time, UTC.
* *name* - str type. Group of weather parameters (Rain, Snow, Extreme etc.)
* *description* - str type. Weather condition within the group.
* *icon_url* - str type. Weather icon url.

__model.InputValidator.InputValidator()__ - class for validation of input data. \
Methods:
* *__is_valid_city_name(city_name)__* - validate city name. (Check if the 
name is in list of valid city names)\
Args: *city_name* - str type. \
Return: bool type. True if city_name is valid, False otherwise.
* *__is_valid_coordinates(lon, lat)__* - validate latitude and longitude. 
(Check if they is numbers in range [-90; 90], [-180; 180] respectively)\
Args: *lon* - float type. Longitude. \
*lat* - float type. Latitude.\
Return: bool type. True if coordinates is valid, False otherwise.

__model.WeatherExceptions.WeatherException(message)__ - class inherits from 
Exception. Custom exception is raised when external API returns an error.
Args: *message* - str type.

__model.WeatherExceptions.InputIsNotValid(message)__ - class inherits from 
Exception. Custom exception is raised when user input is not valid.\
Args: *message* - str type. 

__model.WeatherModel.WeatherModel(date, city_name, temp, pres, hum, 
w_speed, w_deg, vis, clouds, sunrise, sunset, name, description, 
icon_url)__ - class which is base weather model. \
Args: *date* - int type. Timestamp\
*city_name* - str type.\
*temp* - float type. Temperature, Celsius.\
*pres* - float type. Atmospheric pressure, hPa. \
*hum* - float type. Humidity, %.\
*w_speed* - float. type. Wind speed, meter/sec.\
*w_deg* - float type. Wind direction, degrees.\
*vis* - int type or None. Visibility, meter.\
*clouds* - float type. Cloudiness, %.\
*sunrise* - int type. Sunrise timestamp, UTC.\
*sunset* - int type. Sunset timestamp, UTC.\
*name* - str type. Group of weather parameters (Rain, Snow, Extreme etc.)\
*description* - str type. Weather condition within the group.\
*icon_url* - str type. Weather icon. Name of file.\
Fields: 
* *city_name* - str type. Name of city where is the weather.
* *date* - datetime.date type. Date of weather, UTC.
* *temp* - float type. Temperature, Celsius.
* *pressure* - float type. Atmospheric pressure, hPa. 
* *humidity* - float type. Humidity, %.
* *wind_speed* - float type. Wind speed, meter/sec.
* *wind_deg* - float type. Wind direction, degrees.
* *visibility* - int type or None. Visibility, meter.
* *clouds* - float type. Cloudiness, %.
* *sunrise* - datetime type or None. Sunrise datetime, UTC.
* *sunset* - datetime type or None. Sunset datetime, UTC.
* *name* - str type. Group of weather parameters (Rain, Snow, Extreme etc.)
* *description* - str type. Weather condition within the group.
* *icon_url* - str type. Weather icon url.

__model.WeatherRepository.WeatherRepository()__ - class for interact with 
external API.\
Methods:
* *__get_curr_weather_by_city_name(city_name)__* - validate city_name, 
pass request on external API, create WeatherModel from received response. \
Args: *city_name* - str type.\
Return: model.WeatherModel.WeatherModel type.
* *__get_curr_weather_by_location(lon, lat)__* - validate input data, 
pass request on external API, create WeatherModel from received response. \
Args: *lon* - float type. Longitude. \
*lat* - float type. Latitude.\
Return: model.WeatherModel.WeatherModel type.

***
### API
#### __Get current weather data for city by city name:__
*__Description__*:
You can call by city name or city name and country code. 

*__API call__*: \
*../api?city_name={city_name}*\
*../api?city_name={city_name}, {country_code}*

*__Parameters__*:
city_name city name and country code divided by comma, use ISO 3166 
country codes.

*__Example__*:
http://127.0.0.1:5000/api/?city_name=london,%20GB 
#### __Get current weather data for location by geographic coordinates:__
*__Description__*:
You can use float values with dot (.) as decimal separator.

*__API call__*: \
*../api?lon={lon}&lat={lat}*

*__Parameters__*:
__lat, lon__ coordinates of the location of your interest

*__Example__*:
http://127.0.0.1:5000/api/?lat=35.2&lon=139.5 


