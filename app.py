import psycopg2
from psycopg2 import sql

from alerts import get_mta_alerts
from calendar_script import test_push


def get_db_password():
    try:
        with open('/run/secrets/db-password', 'r') as file:
            password = file.read().strip()
        return password
    except FileNotFoundError:
        print("Secret file not found")
        return None
    

db_params = {
    'dbname': 'mta_data',
    'user': 'postgres',
    'password': get_db_password(), 
    'host': 'database',  # Docker service name for PostgreSQL
    'port': '5432'
}


try:
    calendar_formatted_alerts = get_mta_alerts().get('database_formatted_alerts', {})
    print(calendar_formatted_alerts)
    


    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()


    create_table_query = """
        CREATE TABLE IF NOT EXISTS alerts (
            alert_id VARCHAR(30) NOT NULL,
            updated_at INT NOT NULL DEFAULT 0
        );
    """

    cursor.execute(create_table_query)
    print("Table checked/created.")


    insert_query = sql.SQL("""
        INSERT INTO alerts (alert_id, updated_at) 
        VALUES (%s, %s)
    """)

    cursor.executemany(insert_query, calendar_formatted_alerts)
    print("Data inserted.")

    # Commit changes
    conn.commit()

    # test_push()

except Exception as e:
    print("Error:", e)

finally:
    
    if cursor:
        cursor.close()
    if conn:
        conn.close()

