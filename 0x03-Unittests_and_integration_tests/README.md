# Unit and Integration Tests Project

## Overview
This project focuses on learning and implementing unit tests and integration tests in Python for a GitHub organization client application. It involves writing tests for utility functions and a client class that interacts with the GitHub API, using the `unittest` framework, mocking, parameterization, and fixtures. The project is designed for novice developers and is part of the ALX Backend Python curriculum.

## Learning Objectives
By the end of this project, you should be able to explain:
- The difference between unit and integration tests.
- Common testing patterns, including mocking, parameterization, and fixtures.

## Requirements
- **Environment:** Ubuntu 18.04 LTS, Python 3.7
- **Files:**
  - All files must start with `#!/usr/bin/env python3`.
  - Files must end with a newline.
  - Code must follow `pycodestyle` (version 2.5).
  - All files must be executable.
  - All modules, classes, and functions must have proper documentation (verifiable via `python3 -c 'print(__import__("my_module").__doc__)'` and similar commands).
  - Functions and coroutines must be type-annotated.
- **Testing Command:** `python -m unittest path/to/test_file.py`
- **Required Files:**
  - `utils.py`: Contains utility functions (`access_nested_map`, `get_json`, `memoize`).
  - `client.py`: Defines the `GithubOrgClient` class for interacting with the GitHub API.
  - `fixtures.py`: Provides test fixtures for integration tests.
  - Test files: `test_utils.py` and `test_client.py`.

## Project Structure
- **Repository:** `alx-backend-python`
- **Directory:** `0x03-Unittests_and_integration_tests`

## Directory Structure
0x03-Unittests_and_integration_tests/
├── README.md
├── utils.py
├── client.py
├── fixtures.py
├── test_utils.py
└── test_client.py

## File Descriptions
  - `test_utils.py`: Unit tests for `utils.py` functions.
  - `test_client.py`: Unit and integration tests for `client.py` (GithubOrgClient).
  - `utils.py`, `client.py`, `fixtures.py`: Provided source files.

## Tasks
The project consists of the following tasks, each involving specific testing objectives:

1. **Parameterize a Unit Test (Task 0)**:
   - Write unit tests for `utils.access_nested_map` in `test_utils.py`.
   - Use `@parameterized.expand` to test multiple input scenarios.
   - Ensure the method returns expected results for valid inputs.

2. **Parameterize a Unit Test for Exceptions (Task 1)**:
   - Test `utils.access_nested_map` for `KeyError` exceptions using `assertRaises`.
   - Use `@parameterized.expand` to test invalid inputs.

3. **Mock HTTP Calls (Task 2)**:
   - Test `utils.get_json` in `test_utils.py` without making actual HTTP calls.
   - Use `unittest.mock.patch` to mock `requests.get` and verify the output.

4. **Parameterize and Patch (Task 3)**:
   - Test the `memoize` decorator in `test_utils.py`.
   - Mock a method to ensure it is called only once when memoized.

5. **Parameterize and Patch as Decorators (Task 4)**:
   - Test `GithubOrgClient.org` in `test_client.py`.
   - Use `@patch` and `@parameterized.expand` to mock `get_json` and test with different organizations.

6. **Mocking a Property (Task 5)**:
   - Test `GithubOrgClient._public_repos_url` in `test_client.py`.
   - Mock the `org` property to return a known payload and verify the result.

7. **More Patching (Task 6)**:
   - Test `GithubOrgClient.public_repos` in `test_client.py`.
   - Mock `get_json` and `_public_repos_url` to verify the list of repositories.

8. **Parameterize (Task 7)**:
   - Test `GithubOrgClient.has_license` in `test_client.py`.
   - Use `@parameterized.expand` to test license checking logic.

9. **Integration Test: Fixtures (Task 8)**:
   - Set up integration tests for `GithubOrgClient` in `test_client.py`.
   - Use `@parameterized_class` with fixtures from `fixtures.py` and mock `requests.get`.

10. **Integration Tests (Task 9)**:
    - Test `GithubOrgClient.public_repos` and `public_repos(license="apache-2.0")` in `test_client.py`.
    - Verify results against fixtures without external HTTP calls.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/BunnyeNyash/alx-backend-python.git
   cd alx-backend-python/0x03-Unittests_and_integration_tests
   ```

2. **Ensure Dependencies**:
   - Install required packages:
     ```bash
     pip install requests parameterized
     ```

3. **Run Tests**:
   - Execute unit and integration tests:
     ```bash
     python -m unittest test_utils.py
     python -m unittest test_client.py
     ```

## Testing Resources
- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — Mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [How to mock a readonly property with mock?](https://stackoverflow.com/questions/11876727/how-to-mock-a-readonly-property-with-mock)
- [parameterized](https://pypi.org/project/parameterized/)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)
