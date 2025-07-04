import os
import urllib
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()


###################################    FOR  SQL  SERVER     ########################################

# Get environment variables
DB_SQL_SERVER = os.getenv('DB_SQL_SERVER')  # e.g., 'localhost\SQLEXPRESS'
DB_SQL_NAME = os.getenv('DB_SQL_NAME')      # e.g., 'MyDatabase'
DB_SQL_DRIVER = os.getenv('DB_SQL_DRIVER')  # e.g., 'ODBC Driver 17 for SQL Server'

# Build the connection string
params = urllib.parse.quote_plus(
    f"Driver={{{DB_SQL_DRIVER}}};"
    f"Server={DB_SQL_SERVER};"
    f"Database={DB_SQL_NAME};"
    "Trusted_Connection=yes;"
)

# SQLAlchemy connection string
DB_CONNECTION_STRING_FOR_SQL_SERVER = f"mssql+pyodbc:///?odbc_connect={params}"
engine_for_SQL_SERVER = create_engine(DB_CONNECTION_STRING_FOR_SQL_SERVER, fast_executemany=True)
#engine_for_SQL_SERVER = create_engine(f"mssql+pyodbc://{DB_SQL_SERVER}/{DB_SQL_NAME}?driver=ODBC+Driver+17+for+SQL+Server",fast_executemany=True)


###################################    FOR  POSTGRESQL  SERVER     ########################################


POSTGRESQL_username = os.getenv('POSTGRESQL_username')
POSTGRESQL_password = os.getenv('POSTGRESQL_password')
POSTGRESQL_host = os.getenv('POSTGRESQL_host')
POSTGRESQL_port = os.getenv('POSTGRESQL_port')
POSTGRESQL_database = os.getenv('POSTGRESQL_database')

url = f'postgresql+psycopg2://{POSTGRESQL_username}:{POSTGRESQL_password}@{POSTGRESQL_host}:{POSTGRESQL_port}/{POSTGRESQL_database}'

engine_POSTGRESQL = create_engine(url)
