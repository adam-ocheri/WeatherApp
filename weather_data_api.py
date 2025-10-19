import csv
import json


class WeatherDataAPI:

    @staticmethod
    def get_db():
        with open("weather_data.csv", "r") as file:
            csv_reader = csv.DictReader(file)
            data = list(csv_reader)
            return data

    @staticmethod
    def get_weather(cities: [str]):
        data = WeatherDataAPI.get_db()

        result = []
        for city_data in data:
            for city in cities:
                if city == city_data["city"]:
                    result.append(city_data)

        return result


# print(WeatherDataAPI.get_weather(["Berlin", "Sydney"]))
