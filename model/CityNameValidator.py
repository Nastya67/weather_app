import json


class CityNameValidator:
    def __init__(self):
        with open("cities.json", encoding='utf8') as file:
            self.cities = json.loads(file.read())

    def validate(self, city_name):
        pass
