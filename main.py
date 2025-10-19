import argparse
import os
from app import WeatherApp


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Weather App - Poll weather data from multiple sources"
    )

    parser.add_argument(
        "--cities",
        nargs="+",
        default=["Berlin", "Sydney"],  # Default cities
        help="List of cities to get weather data for (default: Berlin Sydney)",
    )

    parser.add_argument(
        "--sources",
        nargs="+",
        type=int,
        choices=[1, 2, 3],
        default=[1, 2, 3],  # Default sources
        help="Data sources: 1=WeatherAPI, 2=WeatherMapAPI, 3=Local CSV (default: 1 2 3)",
    )

    parser.add_argument(
        "--interval",
        type=int,
        default=20,
        help="Polling interval in seconds (default: 20)",
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    # Create and run the weather app
    app = WeatherApp(args.cities, args.sources)


if __name__ == "__main__":
    main()
