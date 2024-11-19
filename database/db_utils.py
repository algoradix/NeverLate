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
        alert_id VARCHAR(30) NOT NULL,
        updated_at INT NOT NULL DEFAULT 0
    );
    """

    execute_query(create_table_query)
    print("Table checked/created.")



def write_MTA_alerts(database_formatted_alerts):

    insert_query = """
    INSERT INTO alerts (alert_id, updated_at) 
    VALUES (%s, %s)
    """

    for alert in database_formatted_alerts:
        execute_query(insert_query, alert)


def check_id_exists(id):
    query = "SELECT 1 FROM alerts WHERE alert_id = %s LIMIT 1;"
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        return result is not None  # Returns True if id exists
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


