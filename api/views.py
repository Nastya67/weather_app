from flask import request, abort
from . import api
from .weather_representation import WeatherApiResponse
from ..model.weather import WeatherException, WeatherRepository


@api.route("/<city_name>", methods=["GET"])
def get_weather_by_city(city_name):
    try:
        weather_rep = WeatherRepository()
        res = weather_rep.get_weather_by_city_name(city_name)
        city_weather = WeatherApiResponse(res, city_name).get_response()
        return city_weather
    except WeatherException as ex:
        abort(404, ex)
