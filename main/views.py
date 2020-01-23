from flask import render_template, request, redirect, abort
from . import main
from .weather_representation import WeatherResponse
from ..model.weather import WeatherException, WeatherRepository


@main.route("/", methods=["GET"])
def index():
    if request.args.get("city_name"):
        return redirect("/"+request.args.get("city_name"))
    return render_template("index.html")


@main.route("/<city_name>", methods=["GET"])
def show_city_weather(city_name):
    try:
        weather_rep = WeatherRepository()
        weather = weather_rep.get_weather_by_city_name(city_name)
        weather_response = WeatherResponse(weather, city_name)
        return render_template("index.html", w=weather_response)
    except WeatherException as ex:
        abort(404, "Wrong city name.")
    except Exception as ex:
        abort(500, "Smth went wrong!")



