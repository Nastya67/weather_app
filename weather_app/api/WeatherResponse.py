class WeatherApiResponse:
    def __init__(self, weather):

        self.json ={"city": weather.city_name,
                    "date": weather.date.strftime("%Y-%m-%d"),
                    "temp": weather.temp,
                    "pressure": weather.pressure,
                    "humidity": weather.humidity,
                    "wind_speed": weather.wind_speed,
                    "wind_deg": weather.wind_deg,
                    "clouds": weather.clouds,
                    "name": weather.name,
                    "description": weather.description,
                    "icon_url": weather.icon_url,
                    "code": 200
                    }
        if weather.sunrise and weather.sunset:
            self.json["sunrise"] = str(weather.sunrise.time())
            self.json["sunset"] = str(weather.sunset.time())
        if weather.visibility:
            self.json["visibility"] = weather.visibility

    def get_response(self):
        return self.json
