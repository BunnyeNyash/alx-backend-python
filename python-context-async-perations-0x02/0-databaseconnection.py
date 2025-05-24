import sqlite3

class DatabaseConnection:
  """A context manager for database connections"""
  
  def __init__(self, db_name):
     """Initialize the context manager with database name"""
    self.db_name = db_name
    self.conn = None

  def __enter__(self):
    """Set up the database connection"""
      self.conn = sqlite3.connect(self.db_name)
      return self.conn

  def __exit__(self, exc_type, exc_value, traceback):
    """Close the database connection"""
    if self.conn:
      self.conn.close()

if __name__ == "__main__":
  # Use the context manager to handle database connection
  with DatabaseConnection('users.db') as conn:
    cursor = conn.cursor()    # cursor to execute SQL queries
    cursor.execute("SELECT * FROM users")  # execute query
    results = cursor.fetchall()    # fetch query results
    print(results)    # print query results

