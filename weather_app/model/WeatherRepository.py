import requests
import json

from .WeatherExceptions import WeatherException, InputIsNotValid
from .WeatherModel import WeatherModel
from .InputValidator import InputValidator
from .secret import API_KEY


class WeatherRepository:
    __URL_curr = "http://api.openweathermap.org/data/2.5/weather"
    __URL_img = "http://openweathermap.org/img/w/{img_name}.png"

    def get_curr_weather_by_city_name(self, city_name):
        if not InputValidator().is_valid_city_name(city_name):
            raise InputIsNotValid("Wrong city name")
        params = self._get_params({"q": city_name})
        weather = self._get_weather(params)
        return self._get_weather_model(weather)

    def get_curr_weather_by_location(self, lon, lat):
        if not InputValidator().is_valid_coordinates(lat=lat, lon=lon):
            raise InputIsNotValid("Wrong coordinates")
        params = self._get_params({"lat": lat, "lon": lon})
        weather = self._get_weather(params)
        return self._get_weather_model(weather)

    def _get_params(self, additional_params):
        params = {"units": "metric", "appid": API_KEY}  # base params
        params.update(additional_params)
        return params

    def _get_weather(self, params):
        resp = requests.get(self.__URL_curr, params=params)
        weather = json.loads(resp.text)
        if weather.get("cod") != 200:
            raise WeatherException("Can't get response from weather api: " + weather.get("message"))
        return weather

    def _get_weather_model(self, weather):
        return WeatherModel(date=weather["dt"],
                            city_name=weather["name"],
                            temp=weather["main"]["temp"],
                            pres=weather["main"]["pressure"],
                            hum=weather["main"]["humidity"],
                            w_speed=weather["wind"]["speed"],
                            w_deg=weather["wind"]["deg"],
                            vis=weather.get("visibility"),
                            clouds=weather["clouds"]["all"],
                            sunrise=weather["sys"]["sunrise"],
                            sunset=weather["sys"]["sunset"],
                            name=weather["weather"][0]["main"],
                            description=weather["weather"][0]["description"],
                            icon_url=self.__URL_img.format(img_name=weather["weather"][0]["icon"]))
