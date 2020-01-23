class WeatherResponse:
    def __init__(self, weather, city_name):
        # there is some transformations of base model
        self.city_name = city_name
        self.date = weather.sunrise.date()
        self.temp = weather.temp
        self.pressure = weather.pressure
        self.humidity = weather.humidity
        self.wind_speed = weather.wind_speed
        self.wind_deg = weather.wind_deg
        self.visibility = weather.visibility
        self.clouds = weather.clouds
        self.sunrise = weather.sunrise.time()
        self.sunset = weather.sunset.time()
        self.name = weather.name
        self.description = weather.description
        self.icon_url = weather.icon_url
