# Python Decorators Project (python-decorators-0x01)

## Overview
This project is designed to deepen understanding of Python decorators by applying them to database operations. It includes tasks to create decorators for logging queries, managing database connections, handling transactions, retrying failed operations, and caching query results. The project uses SQLite as the database and is part of the ALX Backend Python curriculum.

## Repository Information
- **GitHub Repository**: [alx-backend-python](https://github.com/BunnyeNyash/alx-backend-python.git)
- **Directory**: `python-decorators-0x01`

## Directory Structure

```
python-generators-0x00/
├── 0-log_queries.py
├── 1-with_db_connection.py
├── 2-transactional.py
├── 3-retry_on_failure.py
├── 4-cache_query.py
└── README.md                  # Project documentation
```

## File Description
  - `0-log_queries.py`: Logs database queries.
  - `1-with_db_connection.py`: Manages database connections.
  - `2-transactional.py`: Handles transactions with commit/rollback.
  - `3-retry_on_failure.py`: Retries failed database operations.
  - `4-cache_query.py`: Caches query results.

## Prerequisites
- Python 3.8 or higher
- SQLite3 database with a `users` table
- **Python Libraries**:
  - `sqlite3`
  - `functools`
  - `time`

## Project Tasks
1. **Task 0: Logging Database Queries**
   - File: `0-log_queries.py`
   - Objective: Create a `log_queries` decorator to log SQL queries before execution.
   - Key Features: Uses `print` with timestamps via `datetime`.

2. **Task 1: Handle Database Connections with a Decorator**
   - File: `1-with_db_connection.py`
   - Objective: Create a `with_db_connection` decorator to manage SQLite connections.
   - Key Features: Opens and closes connections automatically.

3. **Task 2: Transaction Management Decorator**
   - File: `2-transactional.py`
   - Objective: Create a `transactional` decorator to commit or rollback transactions.
   - Key Features: Ensures data consistency with error handling.

4. **Task 3: Retry Database Queries**
   - File: `3-retry_on_failure.py`
   - Objective: Create a `retry_on_failure` decorator to retry failed operations.
   - Key Features: Configurable retries and delay for transient errors.

5. **Task 4: Cache Database Queries**
   - File: `4-cache_query.py`
   - Objective: Create a `cache_query` decorator to cache query results.
   - Key Features: Uses a dictionary to avoid redundant database calls.

