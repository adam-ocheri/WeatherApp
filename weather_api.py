import requests
import os

# import dotenv

# dotenv.load_dotenv()


class WeatherAPI:

    BASE_URL = "http://api.weatherapi.com/v1"
    WEATHER_ROUTE = "/current.json"

    @staticmethod
    def get_api_key():
        return os.getenv("WEATHER_API_KEY")

    @staticmethod
    def transform_response(weather_data: dict):
        city = weather_data.get("location").get("name")
        temperature = weather_data.get("current").get("temp_c")
        description = weather_data.get("current").get("condition").get("text")

        return {"city": city, "temperature": temperature, "description": description}

    @staticmethod
    def get_weather(cities: [str]):
        result = []
        for city in cities:
            url = f"{WeatherAPI.BASE_URL}{WeatherAPI.WEATHER_ROUTE}?key={WeatherAPI.get_api_key()}&q={city}"
            response = requests.get(url)
            data = WeatherAPI.transform_response(response.json())
            result.append(data)

        return result


# print(WeatherAPI.get_weather("Tel Aviv"))
