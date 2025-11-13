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
        url = make_url(Config.SQLALCHEMY_DATABASE_URI)
        if url.get_backend_name() != "mysql":
            print("The database backend is not MySQL. No action taken.")
            return False
        user = url.username or ""
        password = url.password or ""
        host = url.host or ""
        port = url.port or 5505
        database = url.database

        if not database:
            print("No database name specified in the URI.")
            return False
