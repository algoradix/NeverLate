

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.events"] 

def generate_token():

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

    # try:
    #     service = build("calendar", "v3", credentials=creds)
    #     mta_alerts_calendar_id = 'cf5202eb59df5f34a7607d0175901c028e57c06856386cdffaf88904ea783816@group.calendar.google.com'
        
    #     print(calendar_formatted_alerts)

    #     for i in range(len(calendar_formatted_alerts)):

    #         event = CalendarEvent(service, mta_alerts_calendar_id, calendar_formatted_alerts[i])

    
    #         event.post_events(service)



    # except HttpError as error:
    #     print(f"An error occurred: {error}")


if __name__ == '__main__':
    generate_token()
