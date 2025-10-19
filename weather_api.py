import requests
import os
import dotenv

dotenv.load_dotenv()


class WeatherAPI:

    BASE_URL = "http://api.weatherapi.com/v1"
    WEATHER_ROUTE = "/current.json"

    @staticmethod
    def get_api_key():
        return os.getenv("WEATHER_API_KEY")

    @staticmethod
    def get_weather(city: str):
        url = f"{WeatherAPI.BASE_URL}{WeatherAPI.WEATHER_ROUTE}?key={WeatherAPI.get_api_key()}&q={city}"
        response = requests.get(url)
        return response.json()


# print(WeatherAPI.get_weather("Tel Aviv"))
