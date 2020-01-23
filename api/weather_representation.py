class WeatherApiResponse:
    def __init__(self, weather, city_name):

        self.json = {"city": city_name,
                        "date": weather.sunrise.date(),
                        "temp": weather.temp,
                        "pressure": weather.pressure,
                        "humidity": weather.humidity,
                        "wind_speed": weather.wind_speed,
                        "wind_deg": weather.wind_deg,
                        "visibility": weather.visibility,
                        "clouds": weather.clouds,
                        "sunrise": str(weather.sunrise.time()),
                        "sunset": str(weather.sunset.time()),
                        "name": weather.name,
                        "description": weather.description,
                        "icon_url": weather.icon_url
                        }

    def get_response(self):
        return self.json
