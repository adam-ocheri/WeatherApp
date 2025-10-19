import requests
import os
import dotenv

dotenv.load_dotenv()


class WeathermapAPI:

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    @staticmethod
    def get_api_key():
        return os.getenv("OPENWEATHERMAP_API_KEY")

    @staticmethod
    def get_weather(city: str):
        url = f"{WeathermapAPI.BASE_URL}?q={city}&appid={WeathermapAPI.get_api_key()}"
        response = requests.get(url)
        return response.json()

    @staticmethod
    def get_weather_by_coords(latitude: float, longitude: float):
        url = f"{WeathermapAPI.BASE_URL}?lat={latitude}&lon={longitude}&appid={WeathermapAPI.get_api_key()}"
        response = requests.get(url)
        return response.json()


# print(WeathermapAPI.get_weather("Tel Aviv"))
