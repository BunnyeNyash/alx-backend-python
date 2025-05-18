# 1-batch_processing.py
# ALX Backend Python: Generators - Task 2 - Batch Processing Large Data
# This script connects to a MySQL database, fetches data from the user_data table in batches, and processes it filtering users over 25
# Database: ALX_prodev
# Table: user_data


# Import necessary libraries
import mysql.connector
from mysql.connector import Error


def stream_users_in_batches(batch_size):
    """Generator function to fetch rows from user_data table in batches."""
    try:
        # Connect to the ALX_prodev database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Replace with your actual MySQL root password
            database="ALX_prodev"
        )
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM user_data")
            batch = []
            # First loop: Fetch rows and group into batches
            for row in cursor:
                batch.append({
                    'user_id': row['user_id'],
                    'name': row['name'],
                    'email': row['email'],
                    'age': int(row['age']) if row['age'] is not None else 0
                })
                if len(batch) == batch_size:
                    yield batch
                    batch = []
            # Yield any remaining rows
            if batch:
                yield batch
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

def batch_processing(batch_size):
    """Generator function to process batches and yield users over 25 years old."""
    # Second loop: Iterate over batches
    for batch in stream_users_in_batches(batch_size):
        # Third loop: Filter users over 25 in each batch
        for user in batch:
            if user['age'] > 25:
                yield user