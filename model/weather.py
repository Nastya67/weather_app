import requests
import json
from datetime import datetime as dt

from .secret import API_KEY


class WeatherRepository:
    __URL_curr = "http://api.openweathermap.org/data/2.5/weather"
    #__URL_forecast = "api.openweathermap.org/data/2.5/forecast/daily?q={city_name}&units=metric&cnt=16&appid={api_key}"
    __URL_img = "http://openweathermap.org/img/w/{img_name}.png"

    def __init__(self):
        with open("cities.json", encoding='utf8') as file:
            self.cities = json.loads(file.read())
        self.params = {"units": "metric", "appid": API_KEY}

    def get_weather_by_city_name(self, city_name):
        self.params['q'] = city_name
        resp = requests.get(self.__URL_curr, params=self.params)
        weather = json.loads(resp.text)
        if weather.get("cod") != 200:
            raise WeatherException("Can't get response from weather api: "+weather.get("message"))
        temp, pres, hum = weather["main"]["temp"], weather["main"]["pressure"], weather["main"]["humidity"]
        name, description = weather["weather"][0]["main"], weather["weather"][0]["description"]
        icon_url = self.__URL_img.format(img_name=weather["weather"][0]["icon"])
        vis, clouds = weather["visibility"], weather["clouds"]["all"]
        w_speed, w_deg = weather["wind"]["speed"], weather["wind"]["deg"]
        sunrise, sunset = weather["sys"]["sunrise"], weather["sys"]["sunset"]

        return WeatherModel(temp, pres, hum, w_speed, w_deg, vis, clouds, sunrise, sunset, name, description, icon_url)


class WeatherModel:
    def __init__(self, temp, pres, hum, w_speed, w_deg, vis, clouds, sunrise, sunset, name, description, icon_url):
        self.temp = temp
        self.pressure = pres
        self.humidity = hum
        self.wind_speed = w_speed
        self.wind_deg = w_deg
        self.visibility = vis
        self.clouds = clouds
        self.sunrise = dt.fromtimestamp(sunrise)
        self.sunset = dt.fromtimestamp(sunset)
        self.name = name
        self.description = description
        self.icon_url = icon_url


class WeatherException(Exception):
    def __init__(self, message):
        super().__init__(message)
