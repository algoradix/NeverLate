import requests
import re
import logging
import sys
import os

# script_dir = os.path.dirname(os.path.abspath(__file__))
# project_dir = os.path.abspath(os.path.join(script_dir, '..'))  
# sys.path.append(project_dir)

from database import update_alert_entry_in_db, id_exists, get_updated_at, delete_all_linked_events_in_db, get_db_ids
from calendar_scripts import delete_all_linked_events_in_calendar

logging.basicConfig(level=logging.INFO)

MTA_API_URL_SERVICE_ALERTS = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/camsys%2Fsubway-alerts.json'
DESCRIPTION_TEXT_FILTER = r"(What's happening\?.*\n.*|accessibility icon.*|shuttle bus icon )" 

FRESH_MTA_ALERTS = []
ENCOUNTERED_ALERT_IDS = set()


def format_alert_for_calendar(id_str, alert, alert_id, train_id, updated_at): 
    notification_type = id_str.split(':')[1]
    type_mapping = {'alert': 'alert', 'planned_work': 'planned work'}
    notification_type = type_mapping.get(notification_type, 'unknown')

    active_periods = []
    for period in alert['active_period']:
        time_range = []
        time_range.append(period.get('start', 0))
        time_range.append(period.get('end', 0))
        active_periods.append(time_range)

    header_text = alert['header_text']['translation'][0]['text']

    description_text = alert.get('description_text', {}).get('translation', [])
    if description_text:
        description_text = description_text[0].get('text', "No description available.")
        filtered_text = re.sub(DESCRIPTION_TEXT_FILTER, "", description_text)
        description_text = filtered_text.strip()

    human_readable_active_period = (
        alert.get('transit_realtime.mercury_alert', {}).get('human_readable_active_period', {}).get('translation', [{}])[0].get('text', 'None') )

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
    # print('Calendar format $$$$ \n')
    # print(calendar_format)
    FRESH_MTA_ALERTS.append(calendar_format)

def get_API_MTA_alerts():
    try:
        response = requests.get(MTA_API_URL_SERVICE_ALERTS, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching MTA alerts from API: {e}")
        return {}

def process_alert(single_alert, desired_train):
    alert = single_alert.get('alert', '')
    for informed_entity in alert.get('informed_entity', ''):
        train_id = informed_entity.get('route_id', '') 
        if train_id == desired_train:
            id_str = single_alert.get('id', '')
            alert_id = id_str.split(':')[2]
            updated_at = alert.get('transit_realtime.mercury_alert', {}).get('updated_at', 0)

    
            if not id_exists(alert_id):
                logging.info(f" {alert_id} processed as new")
                update_alert_entry_in_db(alert_id, updated_at)
                format_alert_for_calendar(id_str, alert, alert_id, train_id, updated_at)
            elif updated_at > get_updated_at(alert_id):
                logging.info(f" {alert_id} processed as updated")

                delete_all_linked_events_in_calendar(alert_id)
                delete_all_linked_events_in_db(alert_id)

                update_alert_entry_in_db(alert_id, updated_at)
                format_alert_for_calendar(id_str, alert, alert_id, train_id, updated_at)
            ENCOUNTERED_ALERT_IDS.add(alert_id)



def filter_MTA_alerts(desired_train: str = 'N'):
    MTA_service_alerts = get_API_MTA_alerts().get('entity', [])

    for single_alert in MTA_service_alerts:
        process_alert(single_alert, desired_train)

    db_ids = get_db_ids()
    for db_id in db_ids:
        if db_id not in ENCOUNTERED_ALERT_IDS:
            logging.info(f" {db_id} removed from db and calendar")
            delete_all_linked_events_in_calendar(db_id)
            delete_all_linked_events_in_db(db_id)


    return FRESH_MTA_ALERTS



# if __name__ == '__main__':
#     filter_MTA_alerts()


  





