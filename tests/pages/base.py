import requests

class Base:
    BASE_URL = "https://reqres.in/api"

    def get_method(self, url):
        return requests.get(url)