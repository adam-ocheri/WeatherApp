# server depndencies
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# product API dependencies
from weather_api import WeatherAPI
from weathermap_api import WeathermapAPI
from logz_api import LogzAPI

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    LogzAPI.post_log({"message": "recived request at root route"})

    return {
        "message": "Test integrations API",
        "weather_api_1_test_response": WeatherAPI.get_weather("Tel Aviv"),
        "weather_api_2_test_response": WeathermapAPI.get_weather("Tel Aviv"),
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
