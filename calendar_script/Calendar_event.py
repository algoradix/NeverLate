import pytz
from datetime import datetime


consolidated_active_periods = {}

class Calendar_event:
    def __init__(self, service, calendar_id, notificiation_type, alert_id, train_id, active_periods, header_text, description_text, updated_at, human_readable_active_period):
        
        self.service = service
        self.calendar_id = calendar_id
        self.notificiation_type = notificiation_type
        self.alert_id = alert_id
        self.train_id = train_id
        self.header_text = header_text
        self.description = description_text
        self.updated_at = updated_at
        self.human_readable_active_period = human_readable_active_period
        self.active_periods = active_periods
        self.event = self.initialize_event()

    def color_code_event(self):
        if self.notificiation_type == 'alert':
            return '7'
        
        return '7'
    
    def get_active_periods(self):
        return self.active_periods

    def initialize_event(self):
        self.event = {
            'summary': f'{self.train_id} {self.notificiation_type}',
            'description': self.header_text + '\n' + self.description + '\n' + 'Complete schedule:' + '\n' + self.human_readable_active_period,
            'colorId': self.color_code_event(), 
            'start': {
                'dateTime': '',
                'timeZone': 'America/New_York'
            },
            'end': {
                'dateTime': '',
                'timeZone': 'America/New_York'
            }
        }

        return self.event
    

    def format_rfc3339(self, timestamp):
        dt = datetime.fromtimestamp(timestamp, pytz.timezone('America/New_York'))
        return dt.isoformat()
    

    def post_events(self, service):

        
        for i in range(len(self.active_periods)):


            start = self.format_rfc3339(self.active_periods[i][0])
            end = self.format_rfc3339(self.active_periods[i][1])

            self.event['start']['dateTime'] = start
            self.event['end']['dateTime'] = end
            
            
            time_key = f'{self.active_periods[i][0]}{self.active_periods[i][1]}'



            if time_key not in consolidated_active_periods:
                mark_event = service.events().insert(calendarId=self.calendar_id, body=self.event).execute()
                event_id = mark_event.get('id')
                consolidated_active_periods[time_key] = event_id
            else:
                
                occupying_event_id = consolidated_active_periods[time_key] 

                occupying_event = service.events().get(calendarId=self.calendar_id, eventId=occupying_event_id).execute()

                occupying_event['description'] = occupying_event['description'] + '\n\nNEXT ALERT: \n' + self.event.get('description')

                service.events().update(calendarId=self.calendar_id, eventId=occupying_event_id, body=occupying_event).execute()


        
        return 0









