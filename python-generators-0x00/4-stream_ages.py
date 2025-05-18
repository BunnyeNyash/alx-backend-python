# 4-stream_ages.py
# ALX Backend Python: Generators - Task 4 - Memory-Efficient Aggregation
# # This script connects to a MySQL database, fetches user ages from the user_data table, and calculates the average age using a generator.
# This is a memory-efficient approach, as it does not load all data into memory at once.
# Database: ALX_prodev
# Table: user_data

# Import necessary libraries
import seed
from mysql.connector import Error

def stream_user_ages():
    """Generator function to yield user ages one by one from user_data table."""
    try:
        connection = seed.connect_to_prodev()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT age FROM user_data")
            # First loop: Yield each age
            for row in cursor:
                yield int(row[0]) if row[0] is not None else 0
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

def calculate_average_age():
    """Calculate the average age using the stream_user_ages generator."""
    total_age = 0
    count = 0
    # Second loop: Sum ages and count rows
    for age in stream_user_ages():
        total_age += age
        count += 1
    # Avoid division by zero
    average_age = total_age / count if count > 0 else 0
    return average_age

if __name__ == "__main__":
    average = calculate_average_age()
    print(f"Average age of users: {average}")