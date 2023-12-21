import os

from src.apis.functions.fetch_methods import FetchMethods


class CalendarController:
    def __init__(self, lab):
        self.fetch = FetchMethods()
        self.endpoint = "https://rosa-api-4d498332e4b1.herokuapp.com/api/reserva-lab/"
        self.lab = lab

    def get_events(self):
        return self.fetch.get_request(self.endpoint + "eventos-da-semana/" + self.lab)

    def post_event(self, data: dict):
        return self.fetch.post_request(self.endpoint + "criar-evento", data)

    def get_day_events(self, date):
        return self.fetch.get_request_with_body(self.endpoint + "eventos-do-dia/" + "1", date)
