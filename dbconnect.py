import psycopg2
from psycopg2 import OperationalError

def create_connection():
    try:
        conn = psycopg2.connect(
            dbname="firstdb",
            user="postgres",
            password="Kiranfirstdb",
            host="localhost",
            port="5432"
        )
        print("Connection to PostgreSQL database successful")
        return conn
    except OperationalError as e:
        print(f"Error: {e}")
        return None
    
    
connection = create_connection()


if connection is not None:
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("PostgreSQL database version:", db_version)
    except OperationalError as e:
        print(f"Error: {e}")
    finally:
        if connection is not None:
            connection.close()
            print("Connection closed")