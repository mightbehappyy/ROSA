import os.path
from google.auth.transport.requests import Request
from googleapiclient.errors import HttpError
import apis.CalendarService as CalendarService
from google.oauth2 import service_account
from dotenv import load_dotenv

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]

load_dotenv()


def get_creds():
    creds = None
    creds_file_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    if os.path.exists(creds_file_path):
        creds = service_account.Credentials.from_service_account_file(
            creds_file_path, scopes=SCOPES
        )

    if not creds or not creds.valid:
        if creds and creds.expired:
            creds.refresh(Request())
        else:
            creds = service_account.Credentials.from_service_account_file(
                creds_file_path, scopes=SCOPES
            )

    return creds


calendar_service = CalendarService.CalendarService(get_creds())


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
