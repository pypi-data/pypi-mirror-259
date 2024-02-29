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

# Initialize the Postgres connection
db = Postgres(host="localhost", port="5432", user="postgres", password="password")

# Connect to the 'bookstore' database
db.connect(database="market_data")

# Create the 'books' table
db.create_table("books", {
    "id": "SERIAL PRIMARY KEY",
    "title": "VARCHAR(255) NOT NULL",
    "author": "VARCHAR(255) NOT NULL",
    "price": "DECIMAL(10, 2) NOT NULL",
    "genre": "VARCHAR(255)"
})

# Create the 'orders' table
db.create_table("orders", {
    "id": "SERIAL PRIMARY KEY",
    "book_id": "INTEGER REFERENCES books(id)",
    "quantity": "INTEGER NOT NULL",
    "customer_name": "VARCHAR(255) NOT NULL",
    "order_date": "DATE NOT NULL"
})

# Insert sample books
db.insert("books", {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "price": 15.99, "genre": "Fiction"}).execute()
db.insert("books", {"title": "To Kill a Mockingbird", "author": "Harper Lee", "price": 12.99, "genre": "Fiction"}).execute()

# Insert a sample order
db.insert("orders", {"book_id": 1, "quantity": 2, "customer_name": "John Doe", "order_date": "2023-04-01"}).execute()

# Query all books
print("All books:")
db.select("books",["title"]).execute()

# Query all orders for a specific book
print("Orders for 'The Great Gatsby':")
db.select("orders").where({"book_id": 1}).execute()

# Update the price of a book
db.update("books").set({"price": 14.99}).where({"id": 1}).execute()

# Export books to a CSV file
db.select("books").to_csv("books.csv")

# Export orders to a CSV file
db.select("orders").to_csv("orders.csv")

# Disconnect from the database
db.disconnect()
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