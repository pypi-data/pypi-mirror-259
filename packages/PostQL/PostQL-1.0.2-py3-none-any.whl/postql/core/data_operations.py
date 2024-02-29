import psycopg2
from psycopg2 import sql
from tabulate import tabulate
import csv
import json
import openpyxl
from decimal import Decimal
import pyarrow as pa
import pyarrow.parquet as pq
from termcolor import colored
import boto3
import logging


class DataOperations:
    """
    A class that provides methods for performing data operations on a PostgreSQL database.

    Args:
        connection: The database connection object.
        logger: The logger object for logging messages.

    Attributes:
        connection: The database connection object.
        query: The SQL query string.
        logger: The logger object for logging messages.
    """

    def __init__(self, connection, logger: logging.Logger):
        self.connection = connection
        self.query = None
        self.logger = logger

    def select(self, table, columns=None):
        if columns is None:
            columns_str = "*"
        else:
            columns = [str(col) for col in columns]
            columns_str = ", ".join(map(str, columns))
        self.query = sql.SQL("SELECT {} FROM {}").format(
            sql.SQL(columns_str), sql.Identifier(table)
        )
        return self

    def insert(self, table, data):
        columns = sql.SQL(", ").join(map(sql.Identifier, data.keys()))
        values = sql.SQL(", ").join(map(sql.Literal, data.values()))
        self.query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
            sql.Identifier(table), columns, values
        )
        print(self.query)
        return self

    def update(self, table):
        self.query = sql.SQL("UPDATE {}").format(sql.Identifier(table))
        return self

    def set(self, data):
        set_clause_parts = []
        for key, value in data.items():
            set_clause_parts.append(
                sql.SQL("{} = {}").format(sql.Identifier(key), sql.Literal(value))
            )
        set_clause = sql.SQL(", ").join(set_clause_parts)
        self.query += sql.SQL(" SET {}").format(set_clause)
        return self

    def delete(self, table):
        query = sql.SQL("DELETE FROM {}").format(sql.Identifier(table))
        self.query = query
        return self

    def join(self, table, join_type="INNER"):
        join_clause = sql.SQL(" {} JOIN {}").format(
            sql.SQL(join_type), sql.Identifier(table)
        )
        self.query += join_clause
        return self

    def on(self, condition):
        on_clause = sql.SQL(" ON {}").format(sql.SQL(condition))
        self.query += on_clause
        return self

    def where(self, conditions):
        if conditions:
            where_clause_parts = []
            for key, value in conditions.items():
                if isinstance(value, tuple) and len(value) == 2:
                    operator, value = value
                    where_clause_parts.append(
                        sql.SQL("{} {} {}").format(
                            sql.Identifier(key), sql.SQL(operator), sql.Literal(value)
                        )
                    )
                else:
                    where_clause_parts.append(
                        sql.SQL("{} = {}").format(
                            sql.Identifier(key), sql.Literal(value)
                        )
                    )
            where_clause = sql.SQL(" AND ").join(where_clause_parts)
            self.query += sql.SQL(" WHERE {}").format(where_clause)
        return self

    def order(self, columns, asc=False):
        order_direction = "ASC" if asc else "DESC"
        columns_str = ", ".join(columns)
        self.query += sql.SQL(" ORDER BY {} {}").format(
            sql.SQL(columns_str), sql.SQL(order_direction)
        )
        return self

    def groupby(self, columns):
        columns_str = ", ".join(columns)
        self.query += sql.SQL(" GROUP BY {}").format(sql.SQL(columns_str))
        return self

    def limit(self, limit_value):
        self.query += sql.SQL(" LIMIT {}").format(sql.Literal(limit_value))
        return self

    def execute(self):
        if self.query:
            try:
                self.sql(self.query)
                operation = self.query.split()[0].upper()
                self.logger.info(f"Query executed: {operation} - {self.query}")
                self.query = None
            except Exception:
                pass
        else:
            self.logger.warning("No query to execute.")

    def sql(self, query, _cli=False, _print_results=True):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                if cursor.description is not None:
                    columns = [desc[0] for desc in cursor.description]
                    result = cursor.fetchall()
                    if result:
                        if _print_results:
                            print(tabulate(result, headers=columns, tablefmt="psql"))
                        return result, columns
                    else:
                        self.logger.info("No results found.")
                return True
        except psycopg2.Error as e:
            self.logger.error("Error executing query:\n" + colored(f"{e}", "red"))
            if _cli:
                raise

    def to_csv(self, output_file="output.csv"):
        if self.query:
            try:
                result, columns = self.sql(self.query, _print_results=False)
                if result:
                    with open(output_file, "w", newline="") as f:
                        writer = csv.writer(f)
                        writer.writerow(columns)
                        writer.writerows(result)
                    self.logger.info(f"Results exported to {output_file}.")
                else:
                    self.logger.info("No results found.")
            except Exception as e:
                self.logger.error(f"Error exporting results to CSV: {e}.")
        else:
            self.logger.warning("No query to execute.")

    def to_excel(self, output_file="output.xlsx"):
        if self.query:
            try:
                result, columns = self.sql(self.query, _print_results=False)
                if result:
                    wb = openpyxl.Workbook()
                    ws = wb.active
                    ws.append(columns)
                    for row in result:
                        ws.append(row)
                    wb.save(output_file)
                    self.logger.info(f"Results exported to {output_file}.")
                else:
                    self.logger.info("No results found.")
            except Exception as e:
                self.logger.error(f"Error exporting results to Excel: {e}.")
        else:
            self.logger.warning("No query to execute.")

    def to_json(self, output_file="output.json"):
        if self.query:
            try:
                result, columns = self.sql(self.query, _print_results=False)
                if result:
                    json_result = []
                    for row in result:
                        json_row = {}
                        for i, value in enumerate(row):
                            column_name = columns[i]
                            json_row[column_name] = (
                                float(value) if isinstance(value, Decimal) else value
                            )
                        json_result.append(json_row)

                    with open(output_file, "w") as f:
                        json.dump(json_result, f, indent=4)
                    self.logger.info(f"Results exported to {output_file}.")
                else:
                    self.logger.info("No results found.")
            except Exception as e:
                self.logger.error(f"Error exporting results to JSON: {e}.")
        else:
            self.logger.warning("No query to execute.")

    def to_parquet(self, output_file="output.parquet"):
        try:
            result, columns = self.sql(self.query, _print_results=False)
            if result:
                # Create a pyarrow Table
                table_data = []
                for row in result:
                    table_data.append(row)
                table = pa.Table.from_pydict(
                    {
                        columns[i]: [row[i] for row in table_data]
                        for i in range(len(columns))
                    }
                )

                pq.write_table(table, output_file)
                self.logger.info(f"Results exported to {output_file}.")
            else:
                self.logger.info("No results found.")
        except Exception as e:
            self.logger.error(f"Error exporting results to Parquet: {e}.")

    def upload_to_s3(self, bucket_name, format, filename, acl=None, metadata=None):
        if format.lower() not in ["csv", "excel", "json", "parquet"]:
            self.logger.error(
                "Unsupported format. Please provide one of the following: csv, excel, json, parquet."
            )
            return

        if format.lower() == "csv":
            self.to_csv(output_file=filename)
        elif format.lower() == "excel":
            self.to_excel(output_file=filename)
        elif format.lower() == "json":
            self.to_json(output_file=filename)
        elif format.lower() == "parquet":
            self.to_parquet(output_file=filename)

        s3 = boto3.client("s3")
        try:
            with open(filename, "rb") as data:
                s3.upload_fileobj(
                    data,
                    bucket_name,
                    filename,
                    ExtraArgs={"ACL": acl, "Metadata": metadata},
                )
            self.logger.info(f"File '{filename}' uploaded to bucket '{bucket_name}.'")
        except Exception as e:
            self.logger.error(f"Error uploading file to S3: {e}.")
            raise
