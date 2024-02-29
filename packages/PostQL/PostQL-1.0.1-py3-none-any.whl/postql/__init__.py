import logging
from postql.core.database_management import DatabaseManagement
from postql.core.data_operations import DataOperations

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] [%(name)s] - %(message)s",
)

logger = logging.getLogger(__name__)


class Postgres(DatabaseManagement, DataOperations):
    """
    A class representing a connection to a PostgreSQL database.

    Args:
        host (str): The hostname or IP address of the PostgreSQL server.
        port (int): The port number of the PostgreSQL server.
        user (str): The username for authentication.
        password (str): The password for authentication.
        logger (logging.Logger, optional): The logger object for logging messages. Defaults to logger.

    Attributes:
        params: Additional parameters for the connection.

    Methods:
        connect(database=None, _print_message=True): Connects to the PostgreSQL server.
        disconnect(_print_message=True): Disconnects from the PostgreSQL server.
        create_database(new_database): Creates a new database.
        delete_database(database_to_delete): Deletes a database.
        create_user(username, password, is_superuser=False): Creates a new user.
        switch_user(user, password): Switches to a different user.
        delete_user(username): Deletes a user.
        create_table(name, schema): Creates a new table.
        drop_table(name): Drops a table.
        get_table_schema(table): Retrieves the schema of a table.
        get_connection_details(): Retrieves the connection details.
        execute_query(query, commit=True): Executes a SQL query.
        select(table, columns=None): Selects data from a table.
        where(conditions): Adds a WHERE clause to the query.
        order(columns, asc=False): Adds an ORDER BY clause to the query.
        groupby(columns): Adds a GROUP BY clause to the query.
        limit(limit_value): Adds a LIMIT clause to the query.
        execute(): Executes the query.
        sql(query, commit=False, _cli=False, _print_results=True): Executes a SQL query and returns the result.
        to_csv(output_file="output.csv"): Exports the query result to a CSV file.
        to_excel(output_file="output.xlsx"): Exports the query result to an Excel file.
        to_json(output_file="output.json"): Exports the query result to a JSON file.
        to_parquet(output_file="output.parquet"): Exports the query result to a Parquet file.
        upload_to_s3(bucket_name, format, filename, acl=None, metadata=None): Uploads a file to an S3 bucket.

    """

    def __init__(self, host, port, user, password, logger: logging.Logger = logger):
        super().__init__(host, port, user, password, logger)
        self.params = ()

    def connect(self, database=None, _print_message=True):
        super().connect(database, _print_message)

    def disconnect(self, _print_message=True):
        super().disconnect(_print_message)

    def create_database(self, new_database):
        super().create_database(new_database)

    def delete_database(self, database_to_delete):
        super().delete_database(database_to_delete)

    def create_user(self, username, password, is_superuser=False):
        super().create_user(username, password, is_superuser)

    def switch_user(self, user, password):
        super().switch_user(user, password)

    def delete_user(self, username):
        super().delete_user(username)

    def create_table(self, name, schema):
        super().create_table(name, schema)

    def drop_table(self, name):
        super().drop_table(name)

    def get_table_schema(self, table):
        super().get_table_schema(table)

    def get_connection_details(self):
        super().get_connection_details()

    def _execute_query(self, query):
        super()._execute_query(query)

    def select(self, table, columns=None):
        return super().select(table, columns)

    def insert(self, table, values):
        return super().insert(table, values)

    def update(self, table):
        return super().update(table)

    def delete(self, table):
        return super().delete(table)

    def set(self, data):
        return super().set(data)

    def where(self, conditions):
        return super().where(conditions)

    def order(self, columns, asc=False):
        return super().order(columns, asc)

    def groupby(self, columns):
        return super().groupby(columns)

    def limit(self, limit_value):
        return super().limit(limit_value)

    def execute(self):
        super().execute()

    def sql(self, query, _cli=False, _print_results=True):
        return super().sql(query, _cli, _print_results)

    def to_csv(self, output_file="output.csv"):
        super().to_csv(output_file)

    def to_excel(self, output_file="output.xlsx"):
        super().to_excel(output_file)

    def to_json(self, output_file="output.json"):
        super().to_json(output_file)

    def to_parquet(self, output_file="output.parquet"):
        super().to_parquet(output_file)

    def upload_to_s3(self, bucket_name, format, filename, acl=None, metadata=None):
        super().upload_to_s3(bucket_name, format, filename, acl, metadata)
