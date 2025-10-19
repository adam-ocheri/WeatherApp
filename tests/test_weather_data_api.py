import pytest

from weather_data_api import WeatherDataAPI


class TestWeatherDataAPITransform:

    def test_get_weather_valid_cities(self):
        """Test data retrieval for valid cities"""
        # This tests the implicit transformation from CSV to dict format
        result = WeatherDataAPI.get_weather(["Berlin", "Sydney"])

        assert len(result) == 2
        assert any(city["city"] == "Berlin" for city in result)
        assert any(city["city"] == "Sydney" for city in result)

    def test_get_weather_nonexistent_cities(self):
        """Test data retrieval for cities not in CSV"""
        result = WeatherDataAPI.get_weather(["NonexistentCity"])

        assert result == []
