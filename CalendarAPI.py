import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError
import CalendarService

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def get_creds():
    creds = None
    token = "token.json"

    if os.path.exists(token):
        creds = Credentials.from_authorized_user_file(token, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("secret_file.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open(token, "w") as token_file:
            token_file.write(creds.to_json())

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
