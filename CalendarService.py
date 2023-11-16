import datetime
from googleapiclient.discovery import build
import datetime
from datetime import timedelta
from settings import LAB_LINUX_ID, LAB_WINDOWS_ID


class CalendarService:
    def __init__(self, credentials, service_name="calendar", api_version="v3"):
        self.credentials = credentials
        self.service_name = service_name
        self.api_version = api_version
        self.service = self.build_service()

    def build_service(self):
        return build(
            self.service_name,
            self.api_version,
            credentials=self.credentials,
        )

    def check_current_week_events(self, lab):
        now = datetime.datetime.utcnow()

        start_of_week = now - timedelta(days=now.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        events_result = (
            self.service.events()
            .list(
                calendarId=LAB_WINDOWS_ID if lab == 1 else LAB_LINUX_ID,
                timeMin=start_of_week.isoformat() + "Z",
                timeMax=end_of_week.isoformat() + "Z",
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )

        events = events_result.get("items", [])

        if not events:
            print("No upcoming events found for the current week.")
            return {}

        events_by_day = {}

        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            end = event["end"].get("dateTime", event["end"].get("date"))

            day_name = datetime.datetime.fromisoformat(start).strftime("%A")
            day = datetime.datetime.fromisoformat(start).strftime("%d-%m-%Y")

            start_hour = datetime.datetime.fromisoformat(start).strftime("%H:%M")
            end_hour = datetime.datetime.fromisoformat(end).strftime("%H:%M")

            event_info = {
                "start_hour": start_hour,
                "end_hour": end_hour,
                "summary": event["summary"],
            }

            events_by_day.setdefault(day_name, {}).setdefault(day, []).append(
                event_info
            )
        return events_by_day

    def post_event(self, summary, start, end, date):
        start_time = f"{date}T{start}:00"
        end_time = f"{date}T{end}:00"
        event = {
            "summary": summary,
            "start": {
                "dateTime": start_time,
                "timeZone": "America/Recife",
            },
            "end": {
                "dateTime": end_time,
                "timeZone": "America/Recife",
            },
        }
        try:
            event = (
                self.service.events().insert(calendarId="primary", body=event).execute()
            )

            if event.get("status") == "confirmed":
                print("posted")
            else:
                return print(f"Unexpected response: {event}")
        except Exception as e:
            print(f"An error has occurred: {e}")
