import requests
import os
import json
import dotenv

dotenv.load_dotenv()


class LogzAPI:

    @staticmethod
    def get_token():
        return os.environ.get("LOGZ_TOKEN")

    @staticmethod
    def get_host():
        return os.environ.get("LOGZ_HOST")

    @staticmethod
    def post_log(data: dict):
        log = json.dumps(data)
        url = f"{LogzAPI.get_host()}?token={LogzAPI.get_token()}&type=http-bulk"
        response = requests.post(
            url,
            data=log,
            headers={
                "User-Agent": "logzio-json-logs",
            },
        )
        return response


# res = LogzAPI.post_log('{"message": "---HELLO WORLD 2---"}')
# print(res.text)
