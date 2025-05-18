# Python Generators Project (python-generators-0x00)

## Overview

This project is part of the ALX Backend Python curriculum, focusing on the use of Python generators for memory-efficient data processing with a MySQL database. The tasks implement generator-based solutions to interact with the `ALX_prodev` database, specifically the `user_data` table, which contains user information (`user_id`, `name`, `email`, `age`). The project demonstrates database setup, streaming data, batch processing, lazy pagination, and memory-efficient aggregation while adhering to constraints on loop usage and memory efficiency.

## Objectives

- Set up a MySQL database and populate it with user data from a CSV file.
- Implement generators to stream rows one by one, process data in batches, and paginate data lazily.
- Compute aggregates (e.g., average age) memory-efficiently without loading the entire dataset.
- Use the `yield` keyword and adhere to loop constraints (e.g., 1–3 loops per task).
- Avoid SQL aggregate functions (e.g., `AVG`) where specified.

## Repository

- **GitHub Repository**: [alx-backend-python](https://github.com/BunnyeNyash/alx-backend-python.git)
- **Directory**: `python-generators-0x00`

## Directory Structure

```
python-generators-0x00/
├── seed.py                     # Database setup and seeding script
├── 0-stream_users.py          # Generator to stream user rows
├── 1-batch_processing.py      # Generator for batch processing users over 25
├── 2-lazy_paginate.py         # Generator for lazy pagination
├── 4-stream_ages.py           # Generator for memory-efficient average age
├── user_data.csv              # Sample CSV file for seeding user_data table
├── tests/
│   ├── 0-main.py              # Test script for database setup
│   ├── 1-main.py              # Test script for streaming users
│   ├── 2-main.py              # Test script for batch processing
│   ├── 3-main.py              # Test script for pagination
└── README.md                  # Project documentation
```

Each task has a corresponding test script in the `tests/` folder.

## File Descriptions

- **seed.py**: Defines functions to connect to MySQL, create the `ALX_prodev` database, create the `user_data` table, and insert data from `user_data.csv`.
- **0-stream_users.py**: Implements `stream_users()` to yield user rows one by one using a generator (Task 1).
- **1-batch_processing.py**: Implements `stream_users_in_batches(batch_size)` and `batch_processing(batch_size)` to process users over 25 in batches using generators (Task 2).
- **2-lazy_paginate.py**: Implements `lazy_pagination(page_size)` and `paginate_users(page_size, offset)` to lazily load paginated data using a generator (Task 3).
- **4-stream_ages.py**: Implements `stream_user_ages()` and `calculate_average_age()` to compute the average age memory-efficiently using a generator (Task 4).
- **user_data.csv**: Sample CSV file with user data (format: `user_id,name,email,age`).
- **tests/0-main.py**: Test script for `seed.py`, verifying database setup and data insertion.
- **tests/1-main.py**: Test script for Task 1, printing the first six streamed users.
- **tests/2-main.py**: Test script for Task 2, printing filtered users from batch processing.
- **tests/3-main.py**: Test script for Task 3, printing paginated users.


## Prerequisites

- **Python**: Version 3.8 or higher
- **MySQL**: MySQL Server 8.0 or compatible
- **Python Libraries**:
  - `mysql-connector-python` for database connectivity
- **Operating System**: Tested on Windows (PowerShell) and macOS
- **MySQL Root Password**: Configured for database access



## Database Schema

The `user_data` table in the `ALX_prodev` database has the following schema:

```sql
CREATE TABLE user_data (
    user_id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    age DECIMAL NOT NULL,
    INDEX idx_user_id (user_id)
);
```

## Notes

- **Password Security**: Hardcoding the MySQL password in `seed.py` is not recommended for production. Use environment variables for sensitive credentials.

