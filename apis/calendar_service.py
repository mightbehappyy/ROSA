import datetime
from googleapiclient.discovery import build
import datetime
from datetime import timedelta
from settings import LAB_LINUX_ID, LAB_WINDOWS_ID
from auth.google_api_auth import get_creds


class CalendarService:
    def __init__(self, service_name="calendar", api_version="v3"):
        self.credentials = get_creds()
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
        now = datetime.datetime.utcnow() - timedelta(hours=3)

        if now.weekday() == 5:
            start_of_week = now + timedelta(days=2)
            end_of_week = start_of_week + timedelta(days=5)
        elif now.weekday() == 6:
            start_of_week = now + timedelta(days=1)
            end_of_week = start_of_week + timedelta(days=5)
        else:
            start_of_week = now - timedelta(days=now.weekday())
            end_of_week = start_of_week + timedelta(days=5)

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

        events_by_day = self.format_event_info(events)
        return events_by_day

    def check_future_weeks_schedule(self, lab, value):
        now = (
            datetime.datetime.utcnow() - timedelta(hours=3) + timedelta(days=7 * value)
        )

        if now.weekday() == 5:
            start_of_week = now + timedelta(days=2)
            end_of_week = start_of_week + timedelta(days=5)
        elif now.weekday() == 6:
            start_of_week = now + timedelta(days=1)
            end_of_week = start_of_week + timedelta(days=5)
        else:
            start_of_week = now - timedelta(days=now.weekday())
            end_of_week = start_of_week + timedelta(days=5)

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

        events_by_day = self.format_event_info(events)
        return events_by_day

    def check_for_overlapping_events(self, date, start, end):
        start_time = f"{date}T{start}:00-03:00"
        end_time = f"{date}T{end}:00-03:00"
        print("checar formatação", start_time)
        events_result = (
            self.service.events()
            .list(
                calendarId="primary",
                timeMin=start_time,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )

        events = events_result.get("items", [])
        if not events:
            return False
        else:
            for event in events:
                start = event["start"].get("dateTime", event["start"].get("date"))

                if start < end_time:
                    return True
                else:
                    return False

    def post_event(self, summary, start, end, date):
        try:
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

            event = (
                self.service.events().insert(calendarId="primary", body=event).execute()
            )
            return True

        except Exception as e:
            print(f"An error has occurred on post_event: {e}")
            return False

    def get_day_events(self, date):
        print(f"{date}T00:00:00")
        try:
            start_time = f"{date}T00:00:00-03:00"
            end_time = f"{date}T23:59:00-03:00"
            events_result = (
                self.service.events()
                .list(
                    calendarId="primary",
                    timeMin=start_time,
                    timeMax=end_time,
                    singleEvents=True,
                    orderBy="startTime",
                )
                .execute()
            )
            events = events_result.get("items", [])
            day_events = self.format_event_info(events)
            return day_events
        except Exception as e:
            print(f"An error occurred on get_day_events: {e}")

    def format_event_info(self, events):
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
