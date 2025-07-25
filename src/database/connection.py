import os
from dotenv import load_dotenv
import logging
import snowflake.connector
from sqlalchemy import create_engine
from sqlmodel import Session

load_dotenv()
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

SNOWFLAKE_USER = os.getenv('SNOWFLAKE_USER')
SNOWFLAKE_PASSWORD = os.getenv('SNOWFLAKE_PASSWORD')
SNOWFLAKE_ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT')
SNOWFLAKE_WAREHOUSE = os.getenv('SNOWFLAKE_WAREHOUSE')
SNOWFLAKE_DATABASE = os.getenv('SNOWFLAKE_DATABASE')
SNOWFLAKE_SCHEMA = os.getenv('SNOWFLAKE_SCHEMA_BRONZE')
SNOWFLAKE_ROLE = os.getenv('SNOWFLAKE_ROLE')


SNOWFLAKE_URL = os.getenv("SNOWFLAKE_CONNECTION_STRING")

engine = create_engine(SNOWFLAKE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

# if __name__ == '__main__':
#     conn = get_snowflake_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT CURRENT_VERSION()")
#     print(cursor.fetchone())
#     cursor.close()
#     conn.close()