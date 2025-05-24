import sqlite3

# Define the context manager class for executing queries
class ExecuteQuery:
  def __init__(self, db_name, query, params=()):
    """Initialize with database name, query, and parameters"""
    self.db_name = db_name
    self.query = query
    self.params = params
    self.conn = None
    self.cursor = None

  def __enter__(self):
     """Set up database connection and execute query"""
    self.conn = sqlite3.connect(self.db_name)    # Connect to the database
    self.cursor = self.conn.cursor()    # Create a cursor
    self.cursor.execute(self.query, self.params)    # Execute the query with parameters
    return self.cursor    # Return the cursor to fetch results

  def __exit__(self, exc_type, exc_value, traceback):
    """close cursor and database connection"""
    # Close cursor if it exists
    if self.cursor:
        self.cursor.close()
    # Close connection if it exists
    if self.conn:
        self.conn.close()

if __name__ == "__main__":
  # Use context manager to execute query with parameter
  with ExecuteQuery('users.db', "SELECT * FROM users WHERE age > ?", (25,)) as cursor:
      # Fetch and print all results
      results = cursor.fetchall()
      print(results)
