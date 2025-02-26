from database import create_table
from alerts import filter_MTA_alerts
from calendar_scripts import build_and_post_events



if __name__ == '__main__':
    create_table()

    fresh_MTA_alerts = filter_MTA_alerts('N')

    build_and_post_events(fresh_MTA_alerts)

