# Weather App project

# Description

This project provides an integration with several Weather providers APIs with Logz.io logs monitoring tools.
Each data source is coded with a number:

1. WeatherAPI
2. WeatherMapAPI
3. Local CSV file (db mockup)

# Env File

**`Important !`** This repository contains an `.example.env` file, for you to use your weather provider api keys, and Logz token.

# Run locally

1. install dependencies: `$ pip install -r requirements.txt`
2. run main file `$ python main.py`
3. alternatively, you can provide optional paramaters for the cities and sources you want to use and search under: `$ python main.py --cities Berlin Sydney --sources 1 2 3`

# Run via Docker

1. Run `docker-compose up -d` to run the Weather app in a container
