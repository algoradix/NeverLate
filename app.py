from database import execute_query
from alerts import get_mta_alerts


calendar_formatted_alerts = get_mta_alerts().get('database_formatted_alerts', {})

create_table_query = """
CREATE TABLE IF NOT EXISTS alerts (
    alert_id VARCHAR(30) NOT NULL,
    updated_at INT NOT NULL DEFAULT 0
);
"""
execute_query(create_table_query)
print("Table checked/created.")


insert_query = """
INSERT INTO alerts (alert_id, updated_at) 
VALUES (%s, %s)
"""

for data in calendar_formatted_alerts:
    execute_query(insert_query, data)




   