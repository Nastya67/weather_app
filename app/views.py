from flask import render_template, request, redirect, abort
from . import app
from .WeatherResponse import WeatherResponse
from ..model.WeatherException import WeatherException
from ..model.WeatherRepository import WeatherRepository


@app.route("/", methods=["GET"])
def index():
    if request.args.get("city_name"):
        return redirect("/"+request.args.get("city_name"))
    return render_template("index.html")


@app.route("/<city_name>", methods=["GET"])
def show_city_weather(city_name):
    try:
        weather_rep = WeatherRepository()
        weather = weather_rep.get_curr_weather_by_city_name(city_name)
        weather_response = WeatherResponse(weather)
        return render_template("index.html", w=weather_response)
    except WeatherException as ex:
        abort(404, "Wrong city name.")
    except Exception as ex:
        print(ex)
        abort(500, "Smth went wrong!")



