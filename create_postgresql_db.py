import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os

def create_database():
    dbname = "mydjango"
    user = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('POSTGRESQL_HOST')
    port = 5432

    try:
        print("Connecting to the postgresql server...")
        con = psycopg2.connect(dbname='postgres', user=user, password=password, host=host, port=port)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cur = con.cursor()

        print(f"Checking if the database '{dbname}' exists...")
        cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", (dbname,))
        exists = cur.fetchone()
        if not exists:
            print(f"Database '{dbname}' does not exist, creating database...")
            cur.execute(f"CREATE DATABASE {dbname}")
            print("Database created successfully.")
        else:
            print(f"Database '{dbname}' already exists.")

        cur.close()
        con.close()

    except psycopg2.DatabaseError as e:
        print(f"An error occurred: {e}")
    finally:
        if con:
            con.close()
            print("Database connection closed.")

if __name__ == "__main__":
    create_database()
