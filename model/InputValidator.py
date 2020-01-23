import json
import unidecode
import re


class InputValidator:
    def __init__(self):
        with open("normalized_city_names.json", encoding='utf8') as file:
            self._cities = json.loads(file.read())

    def is_valide_city_name(self, city_name):
        normalized_city_name = unidecode.unidecode(city_name).lower().strip()
        if ", " in normalized_city_name:  # city name with country
            return normalized_city_name in self._cities
        reg_exp = re.compile(normalized_city_name+", [a-z]{2}")
        cities_with_this_name = list(filter(reg_exp.match, self._cities))
        return len(cities_with_this_name) != 0

    def is_valide_coordinates(self, lon, lat):
        try:
            lon_n = float(lon)
            lat_n = float(lat)
        except:
            return False
        if -180 < lon_n < 180 and -90 < lat_n < 90:
            return True
        return False
