import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anu123",
        database="women_safety",
		port=3307
    )