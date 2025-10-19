import requests
import os

# import dotenv

# dotenv.load_dotenv()


class WeathermapAPI:

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    @staticmethod
    def get_api_key():
        return os.getenv("OPENWEATHERMAP_API_KEY")

    @staticmethod
    def transform_response(weather_data: dict):
        city = weather_data.get("name")
        temperature = weather_data.get("main").get("temp")
        description = weather_data.get("weather")[0].get("description")

        return {"city": city, "temperature": temperature, "description": description}

    @staticmethod
    def get_weather(cities: [str]):
        result = []
        for city in cities:
            url = f"{WeathermapAPI.BASE_URL}?q={city}&appid={WeathermapAPI.get_api_key()}&units=metric"
            response = requests.get(url)
            data = WeathermapAPI.transform_response(response.json())
            result.append(data)

        return result


# print(WeathermapAPI.get_weather(["Tel Aviv", "New York"]))
