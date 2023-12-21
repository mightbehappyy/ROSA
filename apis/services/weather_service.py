from apis.controllers.weather_controller import WeatherController


class WeatherService():
    def __init__(self, city):
        self.controller = WeatherController(city)

    def get_weather_stats(self):
        return self.controller.get_weather_stats()

    def get_weather_graph(self):
        return self.controller.get_weather_graph()
