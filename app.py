from database import write_MTA_alerts
from alerts import get_mta_alerts
from calendar_script import test_push

# get_mta_alerts()
database_formatted_alerts = get_mta_alerts().get('database_formatted_alerts', {})
write_MTA_alerts(database_formatted_alerts)

test_push()



