import logging
from database import create_table
from alerts import filter_MTA_alerts
from calendar_scripts import build_and_post_events


def main():
    try:
        create_table()
        logging.info("Table created successfully")

        fresh_MTA_alerts = filter_MTA_alerts('N')
        logging.info("Filtered MTA alerts successfully")

        build_and_post_events(fresh_MTA_alerts)
        logging.info("Posted events to calendar successfully")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()