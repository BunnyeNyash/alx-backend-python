# 2-lazy_paginate.py
# ALX Backend Python: Generators - Task 3 - Lazy Loading Paginated Data
# This script connects to a MySQL database, fetches data from the user_data table in a paginated manner, and yields each page of data.
# This is a lazy loading approach, meaning it only fetches data when needed.
# Database: ALX_prodev  
# Table: user_data

# Import necessary libraries
import seed

def paginate_users(page_size, offset):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_pagination(page_size):
    """Generator function to lazily load pages of user_data rows."""
    offset = 0
    # Single loop to fetch pages
    while True:
        page = paginate_users(page_size, offset)
        if not page:  # Stop if no more rows
            break
        yield page
        offset += page_size