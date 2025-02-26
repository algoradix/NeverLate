import psycopg2

def get_db_password():
    try:
        with open('/run/secrets/db-password', 'r') as file:
            password = file.read().strip()
        return password
    except FileNotFoundError:
        print("Secret file not found")
        return None
    

DB_PARAMS = {
    'dbname': 'mta_data',
    'user': 'postgres',
    'password': get_db_password(), 
    'host': 'database',  # Docker service name for PostgreSQL
    'port': '5432'
}

def get_db_connection():
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        if not conn:
            return None
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None


def execute_query(query, params=None):
    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
    except psycopg2.Error as e:
        print("Database query error:", e)
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def create_table():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS alerts (
        alert_id VARCHAR(30) NOT NULL UNIQUE,
        updated_at INT NOT NULL DEFAULT 0,
        calendar_event_ids TEXT[]
    );
    """
    execute_query(create_table_query)
    print("Table checked/created.")





# def write_MTA_alerts(database_formatted_alerts):

#     insert_query = """
#     INSERT INTO alerts (alert_id, updated_at) 
#     VALUES (%s, %s)
#     """

#     for alert in database_formatted_alerts:
#         execute_query(insert_query, alert)


def id_exists(id):
    query = f"SELECT EXISTS (SELECT 1 FROM alerts WHERE alert_id = %s);"
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute(query, (id,))
            exists = cursor.fetchone()[0]
        return exists

    except Exception as e:
        print(f"Error: {e}")
        return False
    
    finally:
        cursor.close()
        conn.close()


def get_updated_at(id):
    query = "SELECT updated_at FROM alerts WHERE alert_id = %s LIMIT 1;"
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (id,))
        result = cursor.fetchone()

        if result: 
            return result[0]
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
    finally:
        cursor.close()
        conn.close()


def update_alert_entry_in_db(alert_id: str, updated_at: int):
    query = """
    INSERT INTO alerts (alert_id, updated_at) 
    VALUES (%s, %s)
    ON CONFLICT (alert_id) 
    DO UPDATE SET updated_at = EXCLUDED.updated_at;
    """
    try:
        execute_query(query, (alert_id, updated_at))
    except Exception as e:
        print(f"Error updating alert entry: {e}")

def is_alert_new_or_updated(alert_id: str, updated_at: int) -> bool:
    return not id_exists(alert_id) or updated_at > get_updated_at(alert_id)


def link_event_id_to_alert_in_db(alert_id: str, event_id: str):
    query = "UPDATE alerts SET calendar_event_ids = array_append(calendar_event_ids, %s) WHERE alert_id = %s;"
    try:
        execute_query(query, (event_id, alert_id))
    except Exception as e:
        print(f"Error updating alert entry: {e}")

def get_event_ids_linked_to_alert(alert_id: str):
    query = "SELECT calendar_event_ids FROM alerts WHERE alert_id = %s;"
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (alert_id,))
        result = cursor.fetchone()

        if result: 
            return result[0]
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
    finally:
        cursor.close()
        conn.close()

def delete_all_linked_events_in_db(alert_id):
    query = "UPDATE alerts SET calendar_event_ids = array[]::integer[] WHERE alert_id = %s;"
    try:
        execute_query(query, (alert_id,))
    except Exception as e:
        print(f"Error clearing calendar event ids: {e}")


def get_db_ids():
    query = "SELECT alert_id FROM alerts;"
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        if result: 
            return [row[0] for row in result]
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    
    finally:
        cursor.close()
        conn.close()


# if __name__ == '__main__':
#     pass