from fastapi import FastAPI
import psycopg2

app = FastAPI()

#DB connect
DB_HOST = "localhost"
DB_NAME = "firstdb"
DB_USER = "postgres"
DB_PASSWORD = "Kiranfirstdb"
DB_PORT = "5432"

def create_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Connection to PostgreSQL database successful")
        return conn
    except psycopg2.OperationalError as e:
        print(f"Error: {e}")
        return None

@app.get("/employee/")
def get_employee():
    connection = create_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM employee")
            employee = cursor.fetchall()
            return employee
        except psycopg2.Error as e:
            print(f"Error: {e}")
        finally:
            if connection is not None:
                connection.close()
                print("Connection closed")
    return []

# if name == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)