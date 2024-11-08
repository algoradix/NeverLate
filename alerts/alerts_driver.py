import requests
from datetime import datetime
import pytz
import re



def get_mta_alerts():
    mta_alerts = requests.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/camsys%2Fsubway-alerts.json').json()
    

    # eastern = pytz.timezone('US/Eastern')

    filtered_alerts = []



    entity = mta_alerts['entity']

    for i in range(len(entity)):

        notification_type = entity[i]['id'].split(':')[1] # 'alert' or 'planned_work'

        if notification_type == 'planned_work':
            notification_type = 'planned work'

        alert = entity[i]['alert']

        informed_entity = alert['informed_entity']
        for j in range(len(informed_entity)):
            train_id = informed_entity[j].get('route_id', ' ') 
            
            if train_id == 'N':
                
                # active period
                active_periods = []
                for period in alert['active_period']:

                    time_range = []

                    time_range.append(period.get('start', 0))
                    time_range.append(period.get('end', 0))
                    
                    active_periods.append(time_range)
        
                # header text
                header_text = alert['header_text']['translation'][0]['text']

                # description text
                description_text = alert.get('description_text', {}).get('translation', [])
                if description_text:
                    description_text = description_text[0].get('text', "No description available.")

                    filtered_text = re.sub(r"(What's happening\?.*\n.*|accessibility icon.*|shuttle bus icon )", "", description_text, flags=re.DOTALL)

                    description_text = filtered_text.strip()


                # human readable active period
                human_readable_active_period = alert.get('transit_realtime.mercury_alert', {}).get('human_readable_active_period', {})

                if human_readable_active_period:
                    human_readable_active_period = human_readable_active_period.get('translation', [0])[0].get('text', 'None')
                else:
                    human_readable_active_period = 'None'


                formatted_alert = (notification_type, train_id, active_periods, header_text, description_text, human_readable_active_period)
                    
                filtered_alerts.append(formatted_alert)
                
           
            # break

    # for i in range(len(filtered_alerts)):
    #     print(filtered_alerts[i])
    #     print(' ')
    

    return filtered_alerts

# get_mta_alerts()


''' 




'''





