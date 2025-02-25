
import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(script_dir, '..'))  
sys.path.append(project_dir)

import json
import requests



def save_mta_alerts_to_json():
    api_url = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/camsys%2Fsubway-alerts.json'  
    response = requests.get(api_url)
    data = response.json()

    with open('mta_alerts.json', 'w') as f:
        json.dump(data, f, indent=4)

save_mta_alerts_to_json()