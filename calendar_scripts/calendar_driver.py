
import os.path
from calendar_scripts.CalendarEvent import CalendarEvent
from database import get_event_ids_linked_to_alert

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.events"] 
CALENDAR_ID = 'ae1af222e368c7a5c2aebb64c77ecb1214bd92014c65b15cc839fec8fa2ff64b@group.calendar.google.com'

def gog_calendar_init():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("secrets/token.json"):
        creds = Credentials.from_authorized_user_file("secrets/token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "secrets/credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("secrets/token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)
        return service
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

def build_and_post_events(fresh_MTA_alerts):
    service = gog_calendar_init()
    if service == None: print(f"An error occurred")

    for alert in fresh_MTA_alerts:
        event = CalendarEvent(service, CALENDAR_ID, alert)
        event.post_event(service)

def delete_all_linked_events_in_calendar(alert_id):
    service = gog_calendar_init()

    event_ids = get_event_ids_linked_to_alert(alert_id)
    for event_id in event_ids:
        try:
            service.events().delete(calendarId=CALENDAR_ID, eventId=event_id).execute()
        except HttpError as error:
            print(f"An error occurred: {error}")
    