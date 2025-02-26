

import requests
import re
from pprint import pprint



def process_alert(id_str, alert, alert_id, train_id, updated_at, new_or_updated_alerts):
    # notification type
    notification_type = id_str.split(':')[1] # 'alert' or 'planned_work'

    if notification_type == 'planned_work':
        notification_type = 'planned work'
    
    # active periods
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



    calendar_format = {
        'alert_id': alert_id, 
        'notification_type': notification_type, 
        'train_id': train_id, 
        'active_periods': active_periods, 
        'header_text': header_text, 
        'description_text': description_text, 
        'updated_at': updated_at, 
        'human_readable_active_period': human_readable_active_period
    }
    
    database_format = (alert_id, updated_at)
        
    new_or_updated_alerts.append(calendar_format)



def get_mta_alerts():
    mta_alerts = requests.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/camsys%2Fsubway-alerts.json').json()

    print('Timestamp:', mta_alerts['header']['timestamp'])
    

    new_or_updated_alerts = []


    desired_train = 'N'
  

    entities = mta_alerts['entity']


    for entity in entities:

        alert = entity.get('alert', '')
        informed_entities = alert.get('informed_entity', '')

        for informed_entity in informed_entities:
            train_id = informed_entity.get('route_id', ' ') 

            # train_id
            if train_id == desired_train:

                id_str = entity.get('id', '')

                # alert_id
                alert_id = id_str.split(':')[2]

                # updated at
                updated_at = alert.get('transit_realtime.mercury_alert', {}).get('updated_at', 0)
                


                # if id_exists(alert_id) == False:
                #     print(alert_id, ' new id')
                #     process_alert(id_str, alert, alert_id, train_id, updated_at, new_or_updated_alerts, database_formatted_alerts)
                # elif updated_at > get_updated_at(alert_id):
                #     print(updated_at, ' ', get_updated_at(alert_id), ' updated')
                #     process_alert(id_str, alert, alert_id, train_id, updated_at, new_or_updated_alerts, database_formatted_alerts)
                #     # TODO delete old id
                process_alert(id_str, alert, alert_id, train_id, updated_at, new_or_updated_alerts)

        

    return {
        'new_or_updated_alerts': new_or_updated_alerts, 
        }





if __name__ == '__main__':
    # a = len(get_mta_alerts()['new_or_updated_alerts'])
    a = (get_mta_alerts()['new_or_updated_alerts'][4])
    pprint(a)
    
  





