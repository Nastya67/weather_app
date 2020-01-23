import requests
import json

from .WeatherException import WeatherException
from .WeatherModel import WeatherModel
from .secret import API_KEY


class WeatherRepository:
    __URL_curr = "http://api.openweathermap.org/data/2.5/weather"
    __URL_forecast = "api.openweathermap.org/data/2.5/forecast/daily?q={city_name}&cnt=16"
    __URL_img = "http://openweathermap.org/img/w/{img_name}.png"

    def __init__(self):
        self.params = {"units": "metric", "appid": API_KEY}

    def get_curr_weather_by_city_name(self, city_name):
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
        date = weather["dt"]
        return WeatherModel(date, city_name, temp, pres, hum, w_speed, w_deg, vis, clouds, sunrise, sunset,
                            name, description, icon_url)

    def get_forecast_weather_by_city_name(self):
        pass
