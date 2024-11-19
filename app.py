from database import write_MTA_alerts, create_table
from alerts import get_mta_alerts
from calendar_script import test_push


database_formatted_alerts = get_mta_alerts().get('database_formatted_alerts', {})
create_table()
write_MTA_alerts(database_formatted_alerts)

test_push()



