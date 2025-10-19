from weather_api import WeatherAPI
from weathermap_api import WeathermapAPI
from weather_data_api import WeatherDataAPI


"""
# main data source handler class
    sources are refered to as numbers:
    1) WeatherAPI
    2) WeatherMapAPI
    3) Local File (db mock up)
"""


class WeatherDataSources:

    @staticmethod
    def get_weather(cities: [str], sources: [int]):

        if len(cities) == 0:
            return {"warning": "no cities were provided"}

        if len(sources) == 0:
            return {"warning": "no data sources were provided"}

        for source in sources:
            if source != 1 and source != 2 and source != 3:
                return {"warning": "no valid data sources were provided"}

        result = {}

        for source in sources:
            if source == 1:
                source_1_result = WeatherAPI.get_weather(cities)
                result["source_1_result"] = source_1_result
            elif source == 2:
                source_2_result = WeathermapAPI.get_weather(cities)
                result["source_2_result"] = source_2_result
            elif source == 3:
                source_3_result = WeatherDataAPI.get_weather(cities)
                result["source_3_result"] = source_3_result

        return result
