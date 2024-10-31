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
    formatted_alerts = get_mta_alerts()


    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()


    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS alerts (
        train_id VARCHAR(3) NOT NULL,
        header_text VARCHAR(200),
        human_readable_active_period VARCHAR(200),
        converted_active_periods VARCHAR(200),
        description_text TEXT
    );
    """

    cursor.execute(create_table_query)
    print("Table 'users' checked/created.")

    # # Insert sample data
    insert_query = sql.SQL("INSERT INTO alerts (train_id, header_text, human_readable_active_period, converted_active_periods, description_text) VALUES (%s, %s, %s, %s, %s);")
    cursor.executemany(insert_query, formatted_alerts)
    print("Sample data inserted.")

    # Commit changes
    conn.commit()

    test_push()

except Exception as e:
    print("Error:", e)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()

