# seed.py
# ALX Backend Python: Generators - Task 0 - Database Setup
# This script connects to a MySQL database, creates a database and a table, and inserts data from a CSV file into the table. It also handles errors and checks for existing records.
# Database: ALX_prodev
# Table: user_data

# Import necessary libraries
import mysql.connector
import csv
import uuid
from mysql.connector import Error

def connect_db():
    """Connect to the MySQL database server."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your actual MySQL username
            password=""   # Replace with your actual MySQL password
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_database(connection):
    """Create the ALX_prodev database if it does not exist."""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        cursor.close()
    except Error as e:
        print(f"Error creating database: {e}")

def connect_to_prodev():
    """Connect to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your actual MySQL username
            password="bunnyeroot",  # Replace with your actual MySQL password
            database="ALX_prodev"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to ALX_prodev database: {e}")
        return None

def create_table(connection):
    """Create the user_data table if it does not exist."""
    try:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL,
            INDEX idx_user_id (user_id)
        )
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("Table user_data created successfully")
        cursor.close()
    except Error as e:
        print(f"Error creating table: {e}")

def insert_data(connection, data):
    """Insert data from a CSV file into the user_data table if it does not exist."""
    try:
        cursor = connection.cursor()
        with open(data, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row if present
            for row in csv_reader:
                user_id = str(uuid.uuid4()) if len(row) < 1 or not row[0] else row[0]
                name = row[1] if len(row) > 1 else "Unknown"
                email = row[2] if len(row) > 2 else "unknown@example.com"
                age = float(row[3]) if len(row) > 3 and row[3] else 0.0
                # Check if user_id already exists
                cursor.execute("SELECT user_id FROM user_data WHERE user_id = %s", (user_id,))
                if cursor.fetchone() is None:
                    insert_query = """
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                    """
                    cursor.execute(insert_query, (user_id, name, email, age))
            connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error inserting data: {e}")
    except FileNotFoundError:
        print(f"Error: File {data} not found")
    except Exception as e:
        print(f"Error processing CSV: {e}")