from datetime import datetime, timezone
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.events"] 

def test_push():

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
        
        # rfc3339_timestamp = datetime.now(timezone.utc).isoformat()
        event = {
            'summary': 'DOCKER',
            'description': 'A chance to hear more about Google\'s developer products.',
            'colorId': '5', 
            'start': {
                'date': '2024-11-16'
            },
            'end': {
                'date': '2024-11-19'
            }
            }

        mta_alerts_calendarid = 'bbd3d90327a00e53aaff1749fb60d529c844a6892758e453a47a959cad30645b@group.calendar.google.com'
        event = service.events().insert(calendarId=mta_alerts_calendarid, body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))


    except HttpError as error:
        print(f"An error occurred: {error}")


# test_push()
