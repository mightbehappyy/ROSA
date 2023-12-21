from src.apis.controllers.calendar_controller import CalendarController


class CalendarService:
    def __init__(self, lab):
        self.events = CalendarController(lab)

    def get_calendar_week_range(self):
        week_range = self.events.get_events()['weekRange']
        return week_range.replace(' ', ' a ')

    def get_calendar_events(self):
        events = self.events.get_events()['weekEvents']
        events_by_day = {}
        for day_data in events:
            day = day_data["dayOfWeek"]
            if day not in events_by_day:
                events_by_day[day] = []
            events_by_day[day].append(day_data)

        return events_by_day

    def get_todays_events(self, date):
        events = self.events.get_day_events(date)['weekEvents']
        events_by_day = {}
        for day_data in events:
            day = day_data["dayOfWeek"]
            if day not in events_by_day:
                events_by_day[day] = []
            events_by_day[day].append(day_data)

        return events_by_day

    def post_calendar_event(self, summary, start, end, date):
        data = {
            "summary": summary,
            "start": start,
            "end": end,
            "date": date,
        }
        return self.events.post_event(data)
