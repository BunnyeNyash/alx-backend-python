# Context Managers and Asynchronous Programming Project

## Overview
This project focuses on mastering Python context managers and asynchronous programming for database operations. It includes tasks to create class-based context managers for managing database connections and queries, and to execute concurrent asynchronous queries using `aiosqlite`. The project uses SQLite and is part of the ALX Backend Python curriculum.

## Repository Information
- **GitHub Repository**: [alx-backend-python](https://github.com/BunnyeNyash/alx-backend-python.git)
- **Directory**: `python-context-async-perations-0x02`


## Directory Structure
```
python-context-async-perations-0x02/
├── 0-databaseconnection.py
├── 1-execute.py
├── 3-concurrent.py
```

## File Descriptions
  - `0-databaseconnection.py`: Class-based context manager for database connections.
  - `1-execute.py`: Reusable context manager for query execution.
  - `3-concurrent.py`: Concurrent async database queries with `aiosqlite`.

## Requirements
- Python 3.8 or higher
- SQLite3 database with a `users` table
- `aiosqlite` library for Task 2 (`pip install aiosqlite`)
- **Python Libraries**:
  - `sqlite3`
  - `asyncio`

## Project Tasks
1. **Task 0: Custom Class-Based Context Manager for Database Connection**
   - File: `0-databaseconnection.py`
   - Objective: Create a class based context manager to handle opening and closing database connections automatically; `__enter__` and `__exit__`.
   - Key Features: Executes `SELECT * FROM users` and prints results.

2. **Task 1: Reusable Query Context Manager**
   - File: `1-execute.py`
   - Objective: create a reusable context manager that takes a query as input and executes it, managing both connection and the query execution
   - Key Features: Manages connection and query execution in a reusable way.

3. **Task 2: Concurrent Asynchronous Database Queries**
   - File: `3-concurrent.py`
   - Objective: Run multiple database queries concurrently using asyncio.gather;`aiosqlite`
   - Key Features: Fetches all users and users older than 40, executed via `asyncio.run`.

## Notes
- Use `aiosqlite` for Task 2; other tasks use standard `sqlite3`.
