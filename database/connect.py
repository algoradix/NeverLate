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
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None


def execute_query(query, params=None):

    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        if not conn:
            return None
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
        

        