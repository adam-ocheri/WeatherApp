import pytest
from weather_api import WeatherAPI


class TestWeatherAPITransform:

    def test_transform_response_valid_data(self):
        """Test transformation with complete valid data"""
        mock_response = {
            "location": {"name": "Berlin"},
            "current": {"temp_c": 18.5, "condition": {"text": "Scattered clouds"}},
        }

        result = WeatherAPI.transform_response(mock_response)

        assert result == {
            "city": "Berlin",
            "temperature": 18.5,
            "description": "Scattered clouds",
        }

    def test_transform_response_missing_fields(self):
        """Test transformation with missing optional fields"""
        mock_response = {
            "location": {"name": "Berlin"},
            "current": {
                "temp_c": 18.5,
                "condition": {"text": None},  # Missing description
            },
        }

        result = WeatherAPI.transform_response(mock_response)

        assert result["city"] == "Berlin"
        assert result["temperature"] == 18.5
        assert result["description"] is None

    def test_transform_response_malformed_data(self):
        """Test transformation with malformed/missing data"""
        mock_response = {
            "location": {"name": "Berlin"},
            # Missing "current" key
        }

        with pytest.raises(AttributeError):
            WeatherAPI.transform_response(mock_response)
