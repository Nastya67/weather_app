from flask import request, abort
from . import api
from .WeatherResponse import WeatherApiResponse
from ..model.WeatherExceptions import WeatherException, InputIsNotValid
from ..model.WeatherRepository import WeatherRepository


@api.route("/", methods=["GET"])
def get_weather_by_city():
    weather_rep = WeatherRepository()
    try:
        if request.args.get("city_name"):
            res = weather_rep.get_curr_weather_by_city_name(request.args["city_name"])
        elif request.args.get("lon") and request.args.get("lat"):
            res = weather_rep.get_curr_weather_by_location(lon=request.args["lon"], lat=request.args["lat"])
        else:
            abort(404, "You must define city name or coordinates")
        city_weather = WeatherApiResponse(res).get_response()
        return city_weather
    except (WeatherException, InputIsNotValid) as ex:
        abort(404, ex)

