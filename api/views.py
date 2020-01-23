from flask import request, abort
from . import api
from .WeatherResponse import WeatherApiResponse
from ..model.WeatherException import WeatherException
from ..model.WeatherRepository import WeatherRepository


@api.route("/<city_name>", methods=["GET"])
def get_weather_by_city(city_name):
    try:
        weather_rep = WeatherRepository()
        res = weather_rep.get_curr_weather_by_city_name(city_name)
        city_weather = WeatherApiResponse(res).get_response()
        return city_weather
    except WeatherException as ex:
        abort(404, ex)
