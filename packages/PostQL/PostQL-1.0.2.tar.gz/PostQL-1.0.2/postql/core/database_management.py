import psycopg2
from psycopg2 import sql
import logging
from tabulate import tabulate


class DatabaseManagement:
    """
    A class for managing PostgreSQL databases and users.

    Args:
        host (str): The hostname or IP address of the PostgreSQL server.
        port (int): The port number of the PostgreSQL server.
        user (str): The username for authentication.
        password (str): The password for authentication.
        logger (logging.Logger): The logger object for logging messages.

    Attributes:
        host (str): The hostname or IP address of the PostgreSQL server.
        port (int): The port number of the PostgreSQL server.
        user (str): The username for authentication.
        password (str): The password for authentication.
        logger (logging.Logger): The logger object for logging messages.
        connection (psycopg2.extensions.connection): The connection object to the PostgreSQL server.

    """

    def __init__(self, host, port, user, password, logger: logging.Logger):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.logger = logger
        self.connection = None

    def connect(self, database, _print_message=True):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=database,
            )
            self.connection.autocommit = True
            if _print_message:
                self.logger.info(
                    f"Connected to database '{database}' as user '{self.user}'."
                )
        except psycopg2.Error as e:
            self.logger.error(
                f"Error connecting to database '{database}' as user '{self.user}': {e}."
            )
            raise

    def disconnect(self, _print_message=True):
        if self.connection:
            self.connection.close()
            if _print_message:
                self.logger.info("Disconnected from database.")

    def create_database(self, new_database):
        if self.connection.get_dsn_parameters()["dbname"] != "postgres":
            current_database = self.connection.get_dsn_parameters()["dbname"]
            self.connect(database="postgres", _print_message=False)
        query = sql.SQL("CREATE DATABASE {}").format(sql.Identifier(new_database))
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
        except psycopg2.Error as e:
            self.logger.error(f"Failed to create database '{new_database}': {e}.")
        self.connect(database=current_database, _print_message=False)
        self.logger.info(f"Database '{new_database}' created.")

    def delete_database(self, database_to_delete):
        if self.connection.get_dsn_parameters()["dbname"] != "postgres":
            current_database = self.connection.get_dsn_parameters()["dbname"]
            self.connect(database="postgres", _print_message=False)
        query = sql.SQL("DROP DATABASE IF EXISTS {}").format(
            sql.Identifier(database_to_delete)
        )
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
        except psycopg2.Error as e:
            self.logger.error(f"Failed to delete database '{database_to_delete}': {e}.")
        self.connect(database=current_database, _print_message=False)
        self.logger.info(f"Database '{database_to_delete}' deleted.")

    def create_user(self, username, password, is_superuser=False):
        query = sql.SQL("CREATE USER {} WITH PASSWORD {}").format(
            sql.Identifier(username), sql.Literal(password)
        )
        if is_superuser:
            query += sql.SQL(" SUPERUSER")
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.logger.info(f"User '{username}' created.")
        except psycopg2.Error as e:
            self.logger.error(f"Failed to create user '{username}'.")

    def switch_user(self, user, password):
        try:
            current_database = self.connection.get_dsn_parameters()["dbname"]
            self.disconnect(_print_message=False)
            self.user = user
            self.password = password
            self.connect(database=current_database, _print_message=False)
            self.logger.info(f"Switched to user '{user}'.")
        except psycopg2.Error as e:
            self.logger.error(f"Error switching to user '{user}': {e}.")

    def delete_user(self, username):
        query = sql.SQL("DROP USER IF EXISTS {}").format(sql.Identifier(username))
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.logger.info(f"User '{username}' deleted.")
        except psycopg2.Error as e:
            self.logger.error(f"Failed to delete user '{username}'.")

    def create_table(self, name, schema):
        query = sql.SQL("CREATE TABLE IF NOT EXISTS {} ({})").format(
            sql.Identifier(name),
            sql.SQL(", ").join(
                sql.SQL("{} {}").format(sql.Identifier(col), sql.SQL(data_type))
                for col, data_type in schema.items()
            ),
        )
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.logger.info(f"Table '{name}' created.")
        except psycopg2.Error as e:
            self.logger.error(f"Failed to create table '{name}'.")

    def drop_table(self, name):
        query = sql.SQL("DROP TABLE IF EXISTS {}").format(sql.Identifier(name))
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
            self.logger.info(f"Table '{name}' dropped.")
        except psycopg2.Error as e:
            self.logger.error(f"Failed to drop table '{name}': {e}.")
            raise

    def get_table_schema(self, table):
        try:
            query = sql.SQL(
                "SELECT column_name, data_type FROM information_schema.columns WHERE table_name = {}"
            ).format(sql.Literal(table))
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                schema = cursor.fetchall()
            print(
                tabulate(schema, headers=["Column Name", "Data Type"], tablefmt="psql")
            )
        except psycopg2.Error as e:
            self.logger.error(f"Error retrieving schema for table '{table}': {e}.")
            raise

    def get_connection_details(self):
        if self.connection:
            self.logger.info(
                f"Connected to database '{self.connection.get_dsn_parameters()['dbname']}' as user '{self.user}'."
            )
        else:
            self.logger.warning("Not connected to any database.")
