from contextlib import contextmanager
from datetime import datetime
import json
import logging
import math
import os
import pyodbc
import sqlite3
from typing import Dict, List, Optional, Iterator, Any, Union, Hashable

Connection = Union[pyodbc.Connection, sqlite3.Connection]  # Todo: unify in own interface to get autocomplete
Cursor = Union[pyodbc.Cursor, sqlite3.Cursor]
Record = Dict[str, Any]
RecordList = List[Record]


def get_db_connection(server: str, database: str) -> Connection:
    """
    Initiate pyodbc connection to a SQL Server database. This function is intended to be suitable for cloud development:
    in the cloud you use environment variables to log in under a certain username and password, whereas locally you
    simply log in using your AAD credentials.
    You may specify `DB_DRIVER` to a pyodbc-compatible driver name for your system. It defaults
    to `{ODBC Driver 17 for SQL Server}`. If you specify the value `SQLITE` this routine will use the built-in sqlite3
    library to connect instead.
    By default, this connection will try to log into the database with the user account it's executing under. This is
    compatible with AAD login and suitable for local development. If you want to log into a database from another
    environment, you will have to use Windows credentials. Save the username in the environment variable `DB_UID`,
    the password in `DB_PASSWORD`.
    If you add the environment variable `USE_MANAGED_ID` with value `yes`, the managed identity of the azure resource
    will be used to authenticate the connection (Then `DB_UID` & `DB_PASSWORD` will not be necessary anymore).
    """
    driver = os.environ.get('DB_DRIVER', '{ODBC Driver 17 for SQL Server}')
    connection_string = f'Driver={driver};Server={server};Database={database};'
    if driver == 'SQLITE':
        logging.info(f'Connecting to SQLite database {database} because driver=SQLITE. Ignoring server {server}.')

        # Make sqlite3 somewhat well-behaved.
        sqlite3.register_converter('datetime', lambda b: datetime.fromisoformat(b.decode()))
        sqlite3.register_converter('json', json.loads)
        sqlite3.register_adapter(list, json.dumps)
        sqlite3.register_adapter(dict, json.dumps)

        return sqlite3.connect(database, detect_types=sqlite3.PARSE_DECLTYPES)
    elif user := os.environ.get('DB_UID', False):
        logging.info(f'Logging into {database}/{server} as {user}.')
        connection_string += f'Uid={os.environ["DB_UID"]};Pwd={os.environ["DB_PASSWORD"]};'
    elif os.environ.get('DB_USE_MANAGED_ID', 'false').lower() == 'true':
        logging.info(f'Logging into {database}/{server} as managed identity.')
        connection_string += f'Authentication=ActiveDirectoryMsi;'
    else:
        logging.info(f'Logging into {database}/{server} as program user.')
        connection_string += f'Authentication=ActiveDirectoryIntegrated;'

    return pyodbc.connect(connection_string)


@contextmanager
def cursor(db_server: str, db_name: str) -> Iterator[Cursor]:
    """
    Obtain a cursor for a certain database server and database name. Internally uses `get_db_connection`. Use this as
    a context manager, which will handle closing the cursor and the connection. NOTE: this will not handle transaction
    support: most of the time that means you need to commit your transactions yourself!
    Example usage:
    ```
    with cursor('my_server.net', 'test') as c:
        my_data = c.execute('select * from test_database').fetchall()
    ```
    """
    conn = get_db_connection(db_server, db_name)
    c = conn.cursor()
    try:
        if hasattr(c, 'fast_executemany'):
            c.fast_executemany = True
        yield c
    finally:
        c.close()
        conn.close()


def query(c: Cursor, sql: str, data: Optional[tuple] = None) -> RecordList:
    """
    Call `c.execute(sql, data).fetchall()` and format the resulting rowset a list of records of the form
    [{colname: value}].
    """
    if data is None:
        result = c.execute(sql).fetchall()
    else:
        result = c.execute(sql, data).fetchall()
    headers = [name for name, *_ in c.description]
    return [dict(zip(headers, r)) for r in result]


def get_all(c: Cursor, table_name: str) -> RecordList:
    """
    Get all current data from table `table_name`.

    IMPORTANT WARNING: `table_name` is not sanitized. Don't pass untrusted table names to this function!
    """
    return query(c, f'select * from {table_name}')


def validate(data: RecordList) -> RecordList:
    """Validate data records are uniform and have string keys, and replace nans with None."""
    assert len(unique := set(tuple(sorted(r.keys())) for r in data)) == 1, \
        f'Non-uniform list of dictionaries passed, got differing keys {unique}.'
    assert not any(non_str := {k: type(k) for k in data[0].keys() if not isinstance(k, str)}), \
        f'Non-string keys in data, got keys with types {non_str}.'
    return [{k: None if isinstance(v, float) and math.isnan(v) else v for k, v in r.items()} for r in data]


def insert_with_return(
        c: Cursor, table_name: str, data: Record, return_columns: Optional[Union[str, tuple]] = None
) -> Record:
    """
    Insert data into the database, returning a set of return columns. The primary use for this is if you have columns
    generated by your database, like an identity. Returns input record with returned columns added (if any).
    """
    validated_data, *_ = validate([data])
    return_columns = (return_columns,) if isinstance(return_columns, str) else return_columns

    columns = validated_data.keys()
    insert_data = tuple(validated_data[col] for col in columns)
    text_columns = ', '.join(columns)
    placeholders = ', '.join('?' for _ in columns)
    # Dispatch on cursor type for now, pyodbc type is for MSSQL only
    if return_columns is None:
        sql = f'insert into {table_name}({text_columns}) values ({placeholders})'
        c.execute(sql)
        return validated_data
    elif isinstance(c, sqlite3.Cursor):
        text_return_columns = ', '.join(return_columns)
        sql = f'insert into {table_name}({text_columns}) values ({placeholders}) returning {text_return_columns}'
        output = query(c, sql, insert_data)[0]
        return {**validated_data, **output}
    else:
        text_return_columns = ', '.join(f'Inserted.{col}' for col in return_columns)
        sql = f'insert into {table_name}({text_columns}) output {text_return_columns} values ({placeholders})'
        output = query(c, sql, insert_data)[0]
        return {**validated_data, **output}


def write(c: Cursor, table_name: str, data: RecordList, primary_key: Optional[Union[str, tuple]] = None, *,
          update=True, insert=True, delete=True):
    """
    Update data in database table. We check identity based on the keys of the IndexedPyFrame.
    `update`, `insert`, and `delete` control which actions to take. By default, this function emits the correct update,
    insert, and delete queries to make the database table equal to the in-memory table.
    - `update=True` means rows already in the database will be updated with the in-memory data
    - `insert=True` means rows not already in the database will be added from the in-memory data
    - `delete=True` means rows present in the database but not in the in-memory database will be deleted

    If primary_key is None, only inserting is supported.

    IMPORTANT WARNING: `table_name` is not sanitized. Don't pass untrusted table names to this function!
    """
    validated_data = validate(data)

    # Deal with primary key, list of writeable columns, indexed data, data in db
    if primary_key is None:
        assert not update and not delete, 'updating and deleting without specifying a primary key not supported'
        primary_key = tuple()
        validated_data = {i: r for i, r in enumerate(validated_data)}
        columns = tuple(k for k in validated_data[0].keys())
        in_db = set()
    else:
        primary_key = (primary_key,) if isinstance(primary_key, str) else tuple(primary_key)
        assert all(isinstance(r[k], Hashable) for r in validated_data for k in primary_key)
        if any(empty_strings := [name for name in validated_data[0].keys() if any(r[name] == '' for r in validated_data)]):
            logging.warning(f'Columns {empty_strings} contain empty strings. '
                            f'Generally inserting empty strings into a database is a bad idea.')

        # List of writeable columns (for updates we don't try to overwrite the primary key)
        columns = tuple(k for k in validated_data[0].keys() if k not in primary_key)

        # Indexed data on primary key
        validated_data = {tuple(r[i] for i in primary_key): r for r in validated_data}

        # Data present in database
        sql = f'select {", ".join(primary_key)} from {table_name}'
        in_db = {tuple(r[k] for k in primary_key) for r in query(c, sql)}

    if delete and (delete_keys := in_db - validated_data.keys()):
        condition = ' AND '.join(f'{k}=?' for k in primary_key)
        sql = f'delete from {table_name} where {condition}'

        c.executemany(sql, list(delete_keys))

    if update and (update_keys := validated_data.keys() & in_db):
        update_data = [
            (tuple(validated_data[k][col] for col in columns) + tuple(validated_data[k][col] for col in primary_key)) for k in update_keys
        ]

        # Cannot use keyword placeholders because pyodbc doesn't support named paramstyle. Would be better.
        assignment = ', '.join(f'{col}=?' for col in columns)
        pk_cols = ' AND '.join(f'{col}=?' for col in primary_key)
        sql = f'update {table_name} set {assignment} where {pk_cols}'

        if columns:  # If columns is empty, there is nothing to update since we leave the primary key untouched
            c.executemany(sql, update_data)

    if insert and (insert_keys := validated_data.keys() - in_db):
        insert_data = [tuple(validated_data[k][col] for col in columns + primary_key) for k in insert_keys]

        placeholders = ', '.join(f'?' for _ in columns + primary_key)
        text_columns = ', '.join(columns + primary_key)
        sql = f'insert into {table_name}({text_columns}) VALUES ({placeholders})'

        c.executemany(sql, insert_data)
