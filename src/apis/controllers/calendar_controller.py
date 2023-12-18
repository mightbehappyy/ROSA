from src.apis.functions.fetch_methods import FetchMethods


class CalendarController:
    def __init__(self, lab):
        self.fetch = FetchMethods()
        self.endpoint = "http://localhost:8080/api/reserva-lab/"
        self.lab = lab

    def get_events(self):
        return self.fetch.get_request(self.endpoint + "eventos-da-semana/" + self.lab)

    def post_event(self, data: dict):
        return self.fetch.post_request(self.endpoint + "criar-evento", data)
