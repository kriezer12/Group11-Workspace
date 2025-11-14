# create_db_part1.py
# Part 1 by: Franz Angelo R. Loma
# Description: First half of create_db.py

import os
from sqlalchemy.engine.url import make_url
import mysql.connector
from mysql.connector import Error
from config import Config

def create_database_if_not_exists():
    try:
        print(f"Database URI: {Config.SQLALCHEMY_DATABASE_URI}")
        url = make_url(Config.SQLALCHEMY_DATABASE_URI)
        if url.get_backend_name() != "mysql":
            print("The database backend is not MySQL. No action taken.")
            return False
        user = url.username or ""
        password = url.password or ""
        host = url.host or "localhost"
        port = url.port or 3306
        database = url.database

        print(f"Connection details - Host: {host}, Port: {port}, User: {user}, Database: {database}") 

        if not database:
            print("No database name specified in the URI.")
            return False

# create_db_part2.py
# Part 2 by: Carl
# Description: Second half of create_db.py

        conn = mysql.connector.connect(host=host, user=user, password=password, port=port)
        cur = conn.cursor()
        cur.execute(
            f"CREATE DATABASE IF NOT EXISTS {database} "
            f"CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
        )
        print(f"Database {database} is ready.")
        cur.close()
        conn.close()
        return True
    except Error as e:
        print(f"MySQL Error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

if __name__ == "__main__":
    ok = create_database_if_not_exists()
    print("Database creation", "succeeded." if ok else "failed.")