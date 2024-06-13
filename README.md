# Personal Finance Tracker

This project is a CLI application for managing personal finances. It allows users to track income, expenses, and savings with categorized transactions.

### Features

- User authentication and session management
- CRUD operations for transactions (income, expenses, savings)
- Monthly and yearly expense reports
- Visualization of spending trends using graphs

### Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install dependencies using Pipenv:

    ```bash
    pipenv install
    ```

4. Initialize the database:

    ```bash
    pipenv run python -m app.utils init_db
    ```

### Usage

- Run the CLI application:

    ```bash
    pipenv run python app/cli.py
    ```

- Run tests:

    ```bash
    pipenv run pytest

    ```


## Database Schema

The database schema includes the following tables:



### Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
