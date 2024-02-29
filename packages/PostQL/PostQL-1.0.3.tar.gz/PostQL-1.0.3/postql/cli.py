import argparse
import tempfile
import sys
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
import os
import logging
from postql import Postgres
from termcolor import colored

from postql.version import __version__

logging.getLogger("postql").disabled = True


def main():

    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] [%(name)s] - %(message)s",
    )

    parser = argparse.ArgumentParser(
        description="CLI for PostQL",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
    postql connect -H localhost -u postgres -P password -d my_database
    """,
    )

    subparsers = parser.add_subparsers(dest="command")
    parser_connect = subparsers.add_parser("connect", help="Connect to the database")
    parser_connect.add_argument(
        "-H", "--host", type=str, default="localhost", help="Database host"
    )
    parser_connect.add_argument(
        "-p", "--port", type=str, default="5432", help="Database port"
    )
    parser_connect.add_argument(
        "-u", "--user", type=str, required=True, help="Database user"
    )
    parser_connect.add_argument(
        "-P", "--password", type=str, required=True, help="Database password"
    )
    parser_connect.add_argument(
        "-d", "--database", type=str, required=True, help="Database name"
    )

    parser.add_argument(
        "-v", "--version", action="version", version=f"PostQL {__version__}"
    )

    args = parser.parse_args()

    tmp_dir = tempfile.mkdtemp()
    history_file = os.path.join(tmp_dir, ".sql_history")

    if args.command == "connect":
        db = Postgres(
            host=args.host, port=args.port, user=args.user, password=args.password
        )
        try:
            db.connect(database=args.database)
            print("Enter SQL queries or 'exit' to quit:")

            history = FileHistory(history_file)
            while True:
                query = prompt(
                    f"{args.database}> ",
                    history=history,
                )
                if query.lower() == "exit":
                    print("Exiting...")
                    break
                try:
                    db.sql(query, _cli=True)
                except Exception as e:
                    print(colored(f"{e}", "red"))
                    continue
        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit(0)
        except Exception as e:
            logging.error(f"Error connecting to database: {e}")
        finally:
            if os.path.exists(history_file):
                try:
                    os.remove(history_file)
                except Exception as e:
                    logging.error(f"Error deleting history file: {e}")
            if os.path.exists(tmp_dir):
                try:
                    os.rmdir(tmp_dir)
                except Exception as e:
                    logging.error(f"Error removing temporary directory: {e}")
            db.disconnect()


if __name__ == "__main__":
    main()
