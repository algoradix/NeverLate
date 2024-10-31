import requests
from datetime import datetime
import pytz



def get_mta_alerts():
    mta_alerts = requests.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/camsys%2Fsubway-alerts.json').json()
    

    eastern = pytz.timezone('US/Eastern')

    filtered_alerts = []

    for i in range(len(mta_alerts['entity'])):

        

        alert = mta_alerts['entity'][i]['alert']
        informed_entry = alert['informed_entity']
        train_id = informed_entry[0]['route_id']

        converted_active_periods = []
        for period in alert['active_period']:
            start_dt = datetime.fromtimestamp(period['start'], eastern)
            converted_active_periods.append({
                'start': start_dt.strftime('%Y %m %d')
                })
            
            end_dt = period.get('end', 0)
            if end_dt != 0:
                end_dt = datetime.fromtimestamp(end_dt, eastern)
                converted_active_periods.append({
                    'end': end_dt.strftime('%Y %m %d')
                    })
   

        header_text = alert['header_text']['translation'][0]['text']

        description_text = alert.get('description_text', {}).get('translation', [])
        if description_text:
            description_text = description_text[0].get('text', "No description available.")


        human_readable_active_period = alert.get('transit_realtime.mercury_alert', {}).get('human_readable_active_period', {})

        if human_readable_active_period:
            human_readable_active_period = human_readable_active_period.get('translation', [0])[0].get('text', 'None')
        else:
            human_readable_active_period = 'None'

        if train_id == 'N':
            formatted_alert = (train_id, header_text, human_readable_active_period, 'converted_active_periods', description_text)
            
            filtered_alerts.append(formatted_alert)
            # print(header_text)
            # print(human_readable_active_period)
            # print(converted_active_periods)
            # print(" ")
            # print(description_text)
        
    # for i in filtered_alerts:
    #     print(i)
    #     print(" ")


    return filtered_alerts

# get_mta_alerts()





