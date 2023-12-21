import os

from src.apis.functions.fetch_methods import FetchMethods


class WeatherController:
    def __init__(self, city):
        self.fetch = FetchMethods()
        self.endpoint = "https://rosa-api-4d498332e4b1.herokuapp.com/api/weather-consult/"
        self.city = city

    def get_weather_stats(self):
        return self.fetch.get_request(self.endpoint + "current/" + self.city)

    def get_weather_graph(self):
        return self.fetch.get_request(self.endpoint + "forecast/" + self.city)

