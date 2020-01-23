class WeatherResponse:
    def __init__(self, weather):
        # there is may be some transformations of base model
        self.city_name = weather.city_name
        self.date = weather.date
        self.temp = weather.temp
        self.pressure = weather.pressure
        self.humidity = weather.humidity
        self.wind_speed = weather.wind_speed
        self.wind_deg = weather.wind_deg
        self.visibility = weather.visibility
        self.clouds = weather.clouds
        if weather.sunrise and weather.sunset:
            self.sunrise = weather.sunrise.time()
            self.sunset = weather.sunset.time()
        self.name = weather.name
        self.description = weather.description
        self.icon_url = weather.icon_url
