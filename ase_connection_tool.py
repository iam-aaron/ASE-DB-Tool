import os
import pyodbc
from tabulate import tabulate
import csv
from datetime import datetime

# ANSI escape codes for yellow text
YELLOW = '\033[93m'
RESET = '\033[0m'

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def test_ase_connection_no_dsn(server, port, database, user, password):
    conn = None
    try:
        conn_str = f'DRIVER={{Adaptive Server Enterprise}};SERVER={server};PORT={port};DB={database};UID={user};PWD={password}'
        conn = pyodbc.connect(conn_str)
        print("Connection successful!")

        cursor = conn.cursor()

        current_database = database.upper()

        while True:
            sql_command = input(f"Enter your SQL command for database {YELLOW}{current_database}{RESET} (or 'exit' to quit, 'clear' to clear screen): ").strip()
            if sql_command.lower() == 'exit':
                break
            elif sql_command.lower() == 'clear':
                clear_terminal()
                continue
            elif not sql_command:  # Handle Enter key (empty input)
                continue

            if sql_command.lower().startswith('use '):
                new_database = sql_command.split()[1]
                try:
                    cursor.execute(sql_command)
                    current_database = new_database.upper()
                    print(f"Switched to database: {YELLOW}{current_database}{RESET}")
                except Exception as e:
                    print("Error switching database:", str(e))
                continue

            try:
                if sql_command.lower().startswith("set rowcount"):  # Handle row limit command separately
                    cursor.execute(sql_command)
                else:
                    cursor.execute(sql_command)
                    rows = cursor.fetchall()
                    if rows:
                        headers = [column[0] for column in cursor.description]

                        # Create a timestamped filename for each successful query result
                        script_dir = os.path.dirname(__file__)
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                        output_file = os.path.join(script_dir, f"query_results_{timestamp}.csv")

                        with open(output_file, 'w', newline='') as csvfile:
                            csvwriter = csv.writer(csvfile)
                            csvwriter.writerow(headers)
                            csvwriter.writerows(rows)

                        print(f"Results for query: {sql_command} written to {output_file}")
                        print("Results for query:", sql_command)
                        print(tabulate(rows, headers=headers, tablefmt="grid"))
                    else:
                        print("No results returned.")

            except Exception as e:
                print("Error executing query:", str(e))

        # Reset row count to default after executing all queries
        cursor.execute("set rowcount 0")

    except Exception as e:
        print("Failed to connect to the database.")
        print("Error:", str(e))

    finally:
        if conn:
            conn.close()

# Usage
server = '<server>'  
port = '<port>'
user = '<username>'
password = '<password>'
database = '<database_name>'

test_ase_connection_no_dsn(server, port, database, user, password)
