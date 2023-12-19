from src.apis.functions.fetch_methods import FetchMethods


class WeatherController:
    def __init__(self, city):
        self.fetch = FetchMethods()
        self.endpoint = "http://localhost:8080/api/weather-consult/"
        self.city = city

    def get_weather_stats(self):
        return self.fetch.get_request(self.endpoint + "current/" + self.city)

    def get_weather_graph(self):
        return self.fetch.get_request(self.endpoint + "forecast/" + self.city)

