from datetime import datetime, timezone
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# from alerts import get_mta_alerts
from calendar_script.CalendarEvent import CalendarEvent


# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.events"] 

# active_period_queue = {}
# def queue_event_by_active_periods(event, active_period_queue):

#     for i in range(len(event.active_periods)):
            
#             start = event.format_rfc3339(event.active_periods[i][0])
#             end = event.format_rfc3339(event.active_periods[i][1])

#             event.event['start']['dateTime'] = start
#             event.event['end']['dateTime'] = end

#             period_key = (start, end)

#             if period_key not in active_period_queue:
#                  active_period_queue[period_key] = []
#             active_period_queue[period_key].append(event)

#             # print(event.event, "\n")
#             # test_service.events().insert(calendarId=self.calendar_id, body=self.event).execute()



#     return 0



def calendar_head(calendar_formatted_alerts):

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
        mta_alerts_calendar_id = 'f2f40b93027e5974c4e4eff53bb3340d5c4caf25f68ce419f17fd7295825ae3d@group.calendar.google.com'
        


        for i in range(len(calendar_formatted_alerts)):

            event = CalendarEvent(service, mta_alerts_calendar_id, calendar_formatted_alerts[i])

    
            event.post_events(service)



    except HttpError as error:
        print(f"An error occurred: {error}")

