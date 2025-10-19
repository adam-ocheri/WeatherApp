import os
import time
from data_sources import WeatherDataSources
from logz_api import LogzAPI
import signal
import sys

import dotenv

dotenv.load_dotenv()


class WeatherApp:
    def __init__(self):
        self.shutdown_requested = False
        self.setup_signal_handlers()
        self.lifecycle()

    def _signal_handler(self, signum, frame):
        """Handle shutdown signals"""
        print(f"\nReceived signal {signum}. Initiating graceful shutdown...")
        self.shutdown_requested = True

    def setup_signal_handlers(self):
        """Set up signal handlers for graceful shutdown"""
        signal.signal(signal.SIGINT, self._signal_handler)  # Ctrl+C
        signal.signal(signal.SIGTERM, self._signal_handler)  # Termination signal

    def _interruptible_sleep(self, duration):
        """Sleep that can be interrupted by shutdown signal"""
        for _ in range(duration):
            if self.shutdown_requested:
                break
            time.sleep(1)

    def lifecycle(self):
        print("started Weather App lifecycle")
        interval = int(os.environ.get("POLLING_INTERVAL"))
        while not self.shutdown_requested:
            try:
                # time.sleep(interval)
                polled_data = WeatherDataSources.get_weather(
                    ["Berlin", "Sydney"], [1, 2, 3]
                )
                print("Finished Polling Data:")
                print(polled_data)
                LogzAPI.post_log(
                    {"message": "WeatherApp | data poll cycle", "data": polled_data}
                )

                self._interruptible_sleep(interval)
            except Exception as e:
                print(f"Error in lifecycle: {e}")
                if self.shutdown_requested:
                    break

                # Continue with next cycle if not shutting down
                self._interruptible_sleep(interval)

        print("Weather App lifecycle completed gracefully")


WEATHER_APP = WeatherApp()
