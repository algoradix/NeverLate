from database import write_MTA_alerts, create_table
from alerts import get_mta_alerts
from calendar_script import calendar_head


create_table()


alerts = get_mta_alerts()
database_formatted_alerts = alerts.get('database_formatted_alerts', {})
calendar_formatted_alerts = alerts.get('calendar_formatted_alerts', {})


write_MTA_alerts(database_formatted_alerts)

calendar_head(calendar_formatted_alerts)



