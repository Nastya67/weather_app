class WeatherApiResponse:
    def __init__(self, weather):

        self.json ={"city": weather.city_name,
                    "date": weather.date,
                    "temp": weather.temp,
                    "pressure": weather.pressure,
                    "humidity": weather.humidity,
                    "wind_speed": weather.wind_speed,
                    "wind_deg": weather.wind_deg,
                    "visibility": weather.visibility,
                    "clouds": weather.clouds,
                    "name": weather.name,
                    "description": weather.description,
                    "icon_url": weather.icon_url
                    }
        if weather.sunrise and weather.sunset:
            self.json["sunrise"] = str(weather.sunrise.time())
            self.json["sunset"] = str(weather.sunset.time())

    def get_response(self):
        return self.json
