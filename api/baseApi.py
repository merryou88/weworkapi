import requests


class BaseApi:
    def send_api(self,data):
        return requests.request(**data).json()