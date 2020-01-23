from datetime import datetime as dt


class WeatherModel:
    def __init__(self, date, city_name, temp, pres, hum, w_speed, w_deg, vis, clouds, sunrise, sunset,
                 name, description, icon_url):
        self.city_name = city_name
        self.date = dt.fromtimestamp(date).date()
        self.temp = temp
        self.pressure = pres
        self.humidity = hum
        self.wind_speed = w_speed
        self.wind_deg = w_deg
        self.visibility = vis
        self.clouds = clouds
        if sunrise and sunset:
            self.sunrise = dt.fromtimestamp(sunrise)
            self.sunset = dt.fromtimestamp(sunset)
        else:
            self.sunrise = None
            self.sunset = None
        self.name = name
        self.description = description
        self.icon_url = icon_url



