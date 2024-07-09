# ASE Database Connection Tool

This Python script provides a command-line interface for connecting to an Adaptive Server Enterprise (ASE) database, executing SQL commands, and exporting query results to CSV files. 

## Features

- Connect to an ASE database without using a DSN.
- Execute SQL commands interactively.
- Switch between databases dynamically.
- Export query results to timestamped CSV files.
- Clear terminal screen for better readability.

## Requirements

- Python 3.x
- `pyodbc` library
- `tabulate` library

## Installation

1. **Clone the repository** (if applicable):
    ```bash
    git clone https://github.com/your-repository/ase-connection-tool.git
    cd ase-connection-tool
    ```

2. **Install the required packages**:
    ```bash
    pip install pyodbc tabulate
    ```

3. **Ensure the Adaptive Server Enterprise ODBC driver is installed**:
    - Follow the instructions provided by SAP to install the ASE ODBC driver on your system.

## Usage

1. **Edit the config.ini to set your database connection parameters**:
    ```python
    server = '<server>'  
    port = '<port>'
    user = '<username>'
    password = '<password>'
    database = '<database_name>' # You have the ability to switch db later.
    ```

2. **Run the script**:
    ```bash
    python ase_connection_tool.py
    ```

3. **Interact with the tool**:
    - Enter your SQL commands at the prompt.
    - Use the `exit` command to quit the tool.
    - Use the `clear` command to clear the terminal screen.
    - Switch databases by using the `USE <database_name>` command.
    - Results of the queries will be displayed in a tabulated format and saved as CSV files with timestamps.

## Example

```sh
python ase_connection_tool.py
```

### Console Output
```sh
Connection successful!
Enter your SQL command for database DATABASE (or 'exit' to quit, 'clear' to clear screen): SELECT * FROM my_table;
Results for query: SELECT * FROM my_table written to query_results_20230701_123456.csv
Results for query: SELECT * FROM my_table
+----+----------+-----------+
| ID | Name     | Value     |
+----+----------+-----------+
| 1  | Example1 | 123       |
| 2  | Example2 | 456       |
+----+----------+-----------+
Enter your SQL command for database DATABASE (or 'exit' to quit, 'clear' to clear screen):
```

## Notes
- The tool handles empty input gracefully.
- If the USE <database_name> command is used, the tool will attempt to switch the database context.
- Query results are saved as CSV files in the same directory as the script with a unique timestamp.
