# PostQL

PostQL is a Python library and command-line interface (CLI) tool for managing PostgreSQL databases, executing queries, exporting data and interacting with PostgreSQL databases from the command line.

## Features

- Connect to PostgreSQL databases and execute SQL queries interactively via the CLI.
- Perform database management tasks such as creating, deleting databases, users, tables, etc.
- Execute SQL queries directly from Python code using the `Postgres` class.
- Export query results to CSV, Excel, JSON, and Parquet formats.
- Upload exported files to Amazon S3 buckets.

## Installation

You can install PostQL via pip:

```bash
pip install postql
```
## Usage

### Command Line Interface (CLI)

To use the PostQL CLI, simply run `postql` followed by the desired command. Here are some examples:

```bash
# Connect to a database and execute SQL queries interactively
postql connect -H localhost -u postgres -P password -d my_database

# Run query
my_database> Select * from my_table

# Exit the CLI
exit

```
### Python Library

```python
from postql import Postgres

# Create a connection to the database
db = Postgres(host="localhost", port="5432", user="postgres", password="password")

# Connect to a specific database
db.connect(database="my_database")

# Execute SQL queries
db.sql("SELECT * FROM my_table")

# Export query results
db.select(table="users") \
    .where({'age': ('>', 25)}) \
    .to_csv("users_result.csv")

```

## Documentation

- [Methods Documentation](https://abeltavares.github.io/PostQL/methods.html)
- [CLI Documentation](https://abeltavares.github.io/PostQL/cli.html)

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

The codebase of this project follows the [black](https://github.com/psf/black) code style. To ensure consistent formatting, the [pre-commit](https://pre-commit.com/) hook is set up to run the black formatter before each commit.

Additionally, a GitHub Action is configured to automatically run the black formatter on every pull request, ensuring that the codebase remains formatted correctly.

Please make sure to run `pip install pre-commit` and `pre-commit install` to enable the pre-commit hook on your local development environment.

## License 

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) for details.