from googleapiclient.errors import HttpError
from apis.calendar_service import CalendarService
from auth.google_api_auth import get_creds

calendar_service = CalendarService()


def check_calendar(lab: int):
    try:
        return calendar_service.check_current_week_events(lab)
    except HttpError as error:
        print(f"An error occurred: {error}")


def post_event(summary, start, end, date):
    try:
        if calendar_service.check_for_overlapping_events(date, start, end):
            return True
        else:
            if calendar_service.post_event(summary, start, end, date):
                return False
            else:
                return None

    except Exception as e:
        print(f"An error occurred on post event calendar api: {e}")


def get_day_event(date):
    try:
        return calendar_service.get_day_events(date)
    except HttpError as error:
        print(f"An error occurred: {error}")


def get_future_weeks_schedule(lab: int, weeks):
    try:
        return calendar_service.check_future_weeks_schedule(lab, weeks)
    except Exception as e:
        print(f"An error occured on get_future_weeks_schedule {e}")
