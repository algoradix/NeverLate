import pytz
from datetime import datetime
from database import link_event_id_to_alert_in_db

class CalendarEvent:
    def __init__(self, service, calendar_id, calendar_formatted_alert):
        self.grey_color                    = '8'
        self.bold_red_color                = '11'
        self.service                       = service
        self.calendar_id                   = calendar_id
        self.notification_type             = calendar_formatted_alert.get('notification_type')
        self.alert_id                      = calendar_formatted_alert.get('alert_id')
        self.train_id                      = calendar_formatted_alert.get('train_id')
        self.header_text                   = calendar_formatted_alert.get('header_text')
        self.description                   = calendar_formatted_alert.get('description', '')
        self.updated_at                    = calendar_formatted_alert.get('updated_at')
        self.human_readable_active_period  = calendar_formatted_alert.get('human_readable_active_period')
        self.active_periods                = calendar_formatted_alert.get('active_periods')
        self.event                         = self.construct_event()
        # print(self.active_periods)

    def color_code_event(self):
        if self.notification_type == 'alert':
            return self.bold_red_color 
        return self.grey_color
    
    def get_active_periods(self):
        return self.active_periods

    def construct_event(self):
        self.event = {
            'summary': f'{self.train_id} {self.notification_type}',
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
    
    def post_event(self, service):
        for period in self.active_periods:
            
            start_time, end_time = period[0], period[1]
            if end_time == 0: end_time = start_time + 3600 # if no end time, add 60 minutes
            
            start_time = self.format_rfc3339(start_time)
            end_time = self.format_rfc3339(end_time)
            
            self.event['start']['dateTime'] = start_time
            self.event['end']['dateTime'] = end_time
            created_event = service.events().insert(calendarId=self.calendar_id, body=self.event).execute()
            event_id = created_event.get('id')
            link_event_id_to_alert_in_db(self.alert_id, event_id)





