# 0-stream_users.py
# ALX Backend Python: Generators - Task 1 - Stream URows from Database
# Defines a generator to stream rows one by one from the user_data table
# Database: ALX_prodev
# Table: user_data
# Columns: user_id, name, email, age

# Import necessary libraries
import mysql.connector
from mysql.connector import Error

def stream_users():
    """Generator function to stream rows from the user_data table one by one."""
    try:
        # Connect to the ALX_prodev database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="bunnye123winter",  # Replace with your MySQL root password
            database="ALX_prodev"
        )
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)  # Use dictionary cursor for dict output
            cursor.execute("SELECT user_id, name, email, age FROM user_data")
            # Single loop to yield each row
            for row in cursor:
                yield {
                    'user_id': row['user_id'],
                    'name': row['name'],
                    'email': row['email'],
                    'age': int(row['age']) if row['age'] is not None else 0  # Convert DECIMAL to int
                }
            cursor.close()
            connection.close()
    except Error as e:
        print(f"Error connecting to database or fetching data: {e}")
        yield from ()  # Yield empty iterator on error
    except Exception as e:
        print(f"Unexpected error: {e}")
        yield from ()  # Yield empty iterator on error
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()