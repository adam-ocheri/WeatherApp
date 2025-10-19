import pytest
from weathermap_api import WeathermapAPI


class TestWeatherMapAPITransform:

    def test_transform_response_valid_data(self):
        """Test transformation with complete valid data"""
        mock_response = {
            "name": "Sydney",
            "main": {"temp": 22.1},
            "weather": [{"description": "Sunny"}],
        }

        result = WeathermapAPI.transform_response(mock_response)

        assert result == {"city": "Sydney", "temperature": 22.1, "description": "Sunny"}

    def test_transform_response_empty_weather_array(self):
        """Test transformation with empty weather array"""
        mock_response = {
            "name": "Sydney",
            "main": {"temp": 22.1},
            "weather": [],  # Empty array
        }

        with pytest.raises(IndexError):
            WeathermapAPI.transform_response(mock_response)
